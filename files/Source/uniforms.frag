 
    varying vec3 viewDir;
    varying vec3 normal;
    varying vec3 wNormal;
    varying vec3 lightDir[3];
	
	
    uniform sampler2D _Albedo;
    uniform sampler2D _Thickness;
    uniform sampler2D _Alpha;
	
	
    uniform vec3 _DiffuseColor;
    uniform vec3 _TranslucentColor;
	