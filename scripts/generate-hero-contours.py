#!/usr/bin/env python3
"""Regenerate and validate the hero's static contours. Python standard library only.

In elliptical coordinates u=(x-340)/280, v=(y-255)/196, define
q(theta)=1+.075*cos(3*theta)+.045*sin(5*theta), rho=hypot(u,v)/q(theta).
The elevation surface is H=1-rho**2 (H=1 at the centre).
Each contour samples a constant rho, hence constant H. q >= .88 ensures
one positive radius per angle. All loops use the same angular samples.
Validation below checks the actual rounded, straight-segment SVG geometry.
"""
from pathlib import Path
import math
import re

TARGET = Path(__file__).resolve().parents[1] / 'assets/field-map.svg'
COUNT, SAMPLES = 18, 192


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def intersects(a, b, c, d):
    if (max(a[0], b[0]) < min(c[0], d[0]) or
        max(c[0], d[0]) < min(a[0], b[0]) or
        max(a[1], b[1]) < min(c[1], d[1]) or
        max(c[1], d[1]) < min(a[1], b[1])):
        return False
    return cross(a,b,c)*cross(a,b,d) <= 0 and cross(c,d,a)*cross(c,d,b) <= 0


def inside(p, polygon):
    x,y = p
    result = False
    for a,b in zip(polygon, polygon[1:]+polygon[:1]):
        if (a[1] > y) != (b[1] > y):
            if x < a[0]+(y-a[1])*(b[0]-a[0])/(b[1]-a[1]):
                result = not result
    return result


def overlaps_box(a, b, box):
    x0,y0,x1,y1 = box
    corners = [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
    return (x0 <= a[0] <= x1 and y0 <= a[1] <= y1 or
            any(intersects(a,b,c,d) for c,d in zip(corners,corners[1:]+corners[:1])))


loops=[]
for i in range(COUNT):
    radius=.12+.05*i
    loop=[]
    for j in range(SAMPLES):
        theta=math.tau*j/SAMPLES
        q=1+.075*math.cos(3*theta)+.045*math.sin(5*theta)
        loop.append((round(340+280*radius*q*math.cos(theta),1),
                     round(255+196*radius*q*math.sin(theta),1)))
    loops.append(loop)

# Exhaustive segment-pair checks; exclude only adjacent edges of the same loop.
segments=[list(zip(p,p[1:]+p[:1])) for p in loops]
checks=0
for i,edges in enumerate(segments):
    assert len(set(loops[i])) == SAMPLES
    for j,(a,b) in enumerate(edges):
        assert 1 < a[0] < 679 and 1 < a[1] < 519, 'Contour clipping'
        for k in range(j+1,SAMPLES):
            if k==j+1 or (j==0 and k==SAMPLES-1):
                continue
            checks+=1
            assert not intersects(a,b,*edges[k]), 'Self crossing'
        for other in segments[i+1:]:
            for c,d in other:
                checks+=1
                assert not intersects(a,b,c,d), 'Contour intersection'
for inner,outer in zip(loops,loops[1:]):
    assert all(inside(p,outer) for p in inner), 'Non-nested contour'

# Conservative estimated text boxes (monospace 10px, 2px letter spacing),
# padded beyond their expected glyph bounds. Keep them clear of contours,
# the route and other annotations. Browser font metrics still need review.
label_boxes=[(73,420,113,437),(548,61,596,79)]
route=[(104,405),(172,363),(198,295),(274,267),(317,186),(399,197),(443,120),(546,90)]
for box in label_boxes:
    for a,b in [edge for edges in segments for edge in edges]+list(zip(route,route[1:])):
        assert not overlaps_box(a,b,box), 'Label overlap'

paths=''.join('<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in loop)+' Z"/>' for loop in loops)
s=TARGET.read_text()
pattern=r'(<g stroke="#667C73" stroke-opacity=".31" stroke-width=".8">).*?(</g>)'
s,n=re.subn(pattern,lambda m:m[1]+paths+m[2],s,count=1)
assert n==1, 'Contour group not found'
s=re.sub(r'<text x="[^"]+" y="[^"]+">(?:DEPARTURE|HERE)</text>', '<text x="76" y="434">HERE</text>',s)
s=re.sub(r'<text x="[^"]+" y="[^"]+">(?:FURTHER AFIELD|THERE)</text>', '<text x="551" y="76">THERE</text>',s)
TARGET.write_text(s)
print(f'PASS: {COUNT} nested loops; {SAMPLES} vertices per loop; {checks:,} segment-pair checks.')
print('PASS: contour bounds and conservative label boxes clear. SVG regenerated.')
