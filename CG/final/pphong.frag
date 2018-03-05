#version 150

// Phong fragment shader
//
// Contributor:  Meghana Sathish

// INCOMING DATA

// Here is where you should add the variables you need in order
// to propogate data from the vertex shader to the fragment shader
// so that it can do the shading computations

// Material properties of the teapot and quad
uniform vec4 colorAmbience;
uniform float ambienceCE;
uniform vec4 colorDiffusion;
uniform float diffuseCE;
uniform vec4 colorSpecularity;
uniform float specularityExponent;
uniform float specularCE;

// Properties of the light source Illumination properties
uniform vec4 colorLightSource;
uniform vec4 ambientLightColor;

// Properties of the ambient light
uniform vec4 colorLightAmbience;

in vec3 vNorm;     // in model space
in vec4 light;     // in eye space
in vec4 vPos;      // in eye space
in mat4 mvMat;
//in vec4 vPosition;
//in vec4 positionOfSourceLight;
//in mat4 viewMat;
//in vec3 vNormal;

// OUTGOING DATA
out vec4 finalColor;

void main()
{
    mat4 normalmatrix = transpose(inverse (mvMat));
    // vec4 normalCam = normalmatrix * vec4(vNorm, 0.0);
    vec4 normalCam = mvMat * vec4(vNorm, 0.0);
    vec4 N = normalize(normalCam);
	vec4 L = normalize(light-vPos);
	vec4 R = normalize (reflect(-L, N));
    vec4 V = normalize (-vPos);

	// ambient
	vec4 ambient = colorAmbience * ambienceCE * ambientLightColor;
	//colorAmbience * ambienceCE * ambientLightColor;

	// diffuse
	vec4 diffuse = colorLightSource * colorDiffusion * diffuseCE * (dot(N, L));
	// the vectors have been normalized so we can replace cos by dot

	// specular
	vec4 specular = colorLightSource * colorSpecularity * specularCE * pow(max(0.0, dot(V,R)), specularityExponent);

	finalColor = ambient + diffuse + specular ;

	//vPos = mvMat * vPosition;
    //light = viewMat * positionOfSourceLight;
    //vNorm = vNormal;
}
