 
 

    uniform float thicknessPower;
    uniform float thicknessScale;
    uniform float thicknessDistortion;
    uniform float thicknessAmbient;
	
	vec3 translucency( sampler2D tex, vec3 thicknessColor, vec2 vUv, vec3 N, vec3 V, vec3 vLightDir, vec3 lCol )
    {             
        // accumulo
        float thicknessCutoff = 0.75;
        float thicknessDecay = 1.;        
                
        vec3 L = normalize(vLightDir);
        float d = length(vLightDir);
        
        // attenuazione
        float kC = 0.5;
		float kL = 0.05;
		float kQ = 0.0001;
        
        float lightAtten = (1.0 / (kC + kL*d + kQ*d*d));
        
        // calcolo translucenza
        
        vec3 thickness = thicknessColor *texture2D(tex, vUv).rgb/2.;
        vec3 LTLight = normalize(L+ (N*thicknessDistortion));        
        float LTDot = pow(clamp(dot(V, -LTLight),0.,1.), thicknessPower) * thicknessScale;
		
        vec3 LT = lightAtten * (LTDot + thicknessAmbient) * thickness;
        vec3 reflectedLightDirectDiffuse = _TranslucentColor*lCol *LT;
        
        return reflectedLightDirectDiffuse;        
    }    
