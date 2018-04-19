

float celShader (vec3 wN, vec3 L) 
{   
	float light = dot(wN,normalize(L));
	light = pow(light*2., 3.)/2.;
	light = max(light,0.);
	return (1.+light/3.5);
}