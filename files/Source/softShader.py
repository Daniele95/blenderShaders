from bge import logic as g
import math
import mathutils
import time
import sys
sys.path.insert(0, 'Source')
from loadFile import loadFile
 
 
cont = g.getCurrentController()
scene = g.getCurrentScene()
l = scene.objects['gameLight'].position

    
VertexShader = """

    void main()
    {            
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        gl_TexCoord[0] = gl_MultiTexCoord0;
        
        wPos = vec3(_ModelMatrix * gl_Vertex);
        viewDir = normalize ( -wPos + _CameraPos.xyz );
    
	    wNormal = m3(_ModelMatrix)*gl_Normal;
        wNormal = normalize(wNormal);
        normal = gl_Normal;
        lightDir = _LightPos - wPos;
    }
"""
 
FragmentShader = """


    void main()
    {          
        vec2 uv = gl_TexCoord[0].st;
        
        vec3 color = texture2D(_Albedo, uv).xyz;
        vec3 outGoingLight = translucency(_Thickness, uv, normal, viewDir, lightDir );
        vec3 diffuse = celShader(wNormal, lightDir) * color/4.;
        
        vec4 final = vec4 (diffuse,1.) 
             + vec4(outGoingLight, 1.);
        gl_FragColor = final;
    }

"""

lc = scene.objects['gameLight'].color
le = scene.objects['gameLight'].energy
for i in range(0, 3):
    lc[i] = lc[i] * le

mesh = cont.owner.meshes[0]

c = mesh.materials[0].diffuseColor
cI = mesh.materials[0].diffuseIntensity

t = mesh.materials[1].diffuseColor
tI = mesh.materials[1].diffuseIntensity




uniforms =loadFile('Source/uniforms.vert')
m3 = loadFile('Source/m3.vert')
VertexShader = uniforms + m3 + VertexShader

uniforms = loadFile('Source/uniforms.frag')    
celShader = loadFile('Source/celShader.frag')
translucency = loadFile('Source/translucency.frag')
FragmentShader = uniforms + celShader + translucency + FragmentShader



for mat in mesh.materials:
    shader = mat.getShader()
    if shader != None:
        if not shader.isValid():
            shader.setSource(VertexShader, FragmentShader, 1)
        c = mat.diffuseColor
        shader.setUniformDef('_ModelMatrix', g.MODELMATRIX)
        shader.setUniformfv('_LightPos', [l.x,l.y,l.z])
        shader.setSampler('_Albedo', 0)
        shader.setSampler('_Thickness', 1)
        shader.setUniformDef('_CameraPos', g.CAM_POS)
        shader.setUniform3f("_Albedo", c.r* cI, c.g* cI, c.b * cI)
        shader.setUniform3f("_TranslucentColor", t.r*tI, t.g*tI, t.b*tI )
        shader.setUniform3f("_PointLightColor", lc[0], lc[1], lc[2])
        shader.setUniform1f('thicknessPower', cont.owner['thicknessPower'])
        shader.setUniform1f('thicknessScale', cont.owner['thicknessScale'])
        shader.setUniform1f('thicknessDistortion', cont.owner['thicknessDistortion'])
        shader.setUniform1f('thicknessAmbient', cont.owner['thicknessAmbient'])

