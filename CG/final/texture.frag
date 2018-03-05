#version 150

// Texture mapping vertex shader
//
// Contributor:  Meghana Sathish

// INCOMING DATA
in vec4 color;
in vec2 texCoord;
uniform sampler2D img1;

// Material properties of the teapot and quad

uniform float ambienceCE;
uniform float diffuseCE;
uniform float specularityExponent;
uniform float specularCE;

// Properties of the light source Illumination properties
uniform vec4 colorLightSource;
uniform vec4 ambientLightColor;

in vec3 vNorm;     // in model space
in vec4 light;     // in eye space
in vec4 vPos;      // in eye space
in mat4 mvMat;

// OUTGOING DATA

out vec4 finalColor;

void main()
{
    vec4 IntermediateColor =  texture( img1, texCoord );

    mat4 normalmatrix = transpose(inverse (mvMat));
    // vec4 normalCam = normalmatrix * vec4(vNorm, 0.0);
    vec4 normalCam = mvMat * vec4(vNorm, 0.0);
    vec4 N = normalize(normalCam);
	vec4 L = normalize(light-vPos);
	vec4 R = normalize (reflect(-L, N));
    vec4 V = normalize (-vPos);


	// ambient
	vec4 ambient = IntermediateColor * ambienceCE * ambientLightColor;
	//colorAmbience * ambienceCE * ambientLightColor;

	// diffuse
	vec4 diffuse = colorLightSource * IntermediateColor * diffuseCE * (dot(N, L));
	// the vectors have been normalized so we can replace cos by dot

	// specular
	vec4 specular = colorLightSource * IntermediateColor * specularCE * pow(max(0.0, dot(V,R)), specularityExponent);

	finalColor = ambient + diffuse + specular ;
}
