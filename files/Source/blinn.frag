    vec3 Blinn(vec3 N,vec3 V, vec3 vLightDir )
    {  
    	float shininess = 500.0;
        vec3 L = normalize(vLightDir);
        float NdotL = max( dot(N, L), 0.0 );
        
         // attenuazione
        float kC = 0.5;
		float kL = 0.05;
		float kQ = 0.0001;    
		float d = length( vLightDir );
	    float LightAttenuation = (1.0 / (kC + kL*d + kQ*d*d));
				
		vec3 diffcomp = _MainColor.rgb * _PointLightColor * NdotL;
		vec3 H = normalize(V + L);
		vec3 specular = vec3( clamp( 6.0*pow( max(dot(N, H), 0.0), shininess ), 0.0, 1.0 ) ) ;

		return (diffcomp + specular) * LightAttenuation;
    }