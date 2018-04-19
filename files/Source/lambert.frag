    vec3 lambert( sampler2D tex, vec2 uv, vec3 N, vec3 L )
    {  
        vec3 nrmN = normalize( N );
        vec3 nrmL = normalize( L );
        float result = dot( nrmN, nrmL );
        return vec3( texture2D( tex, uv ) ) * max( result, 0.0 );
    }