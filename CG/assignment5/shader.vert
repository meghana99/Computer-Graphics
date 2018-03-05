//
// Vertex shader for the transformation assignment
//
// Created by Warren R. Carithers 2016/04/22.
//
// Contributor:  Meghana Sathish (mxs7620@rit.edu)
//

#version 150

// attribute:  vertex position
in vec4 vPosition;

// add other global shader variables to hold the
// parameters your application code is providing

//Variable to toggle between orthogonal and frustum projection.
uniform int typeOfProjection;

//variables to store the scaling, rotation and translation units along x, y and z directions.
uniform vec3 scale, rotate, translate, eye, look, up;

//variables to store the camera and eye positions.
float left = -1.0, right = 1.0, top = 1.0, bottom = -1.0, near = 0.9, far = 4.5;

// Method declaration for getOrtho() method that will be called to get the orthogonal projection matrix
mat4 getOrtho();

// Method declaration for getFrust() method that will be called to get the Frustum/Perspective projection matrix
mat4 getFrust();

void main()
{
    // By default, no transformations are performed.
    gl_Position =  vPosition;
    // Vector to store the radian values of all the angles in x y and z direction.
    vec3 theta = radians(rotate);
    // Vector to store the cos of the angles in all the x, y and z directions.
    vec3 cosTheta = cos(theta);
    // Vector to store the sin of the angles in all the x, y and z directions.
    vec3 sinTheta = sin(theta);
    // Vector to store the final transformation matrix after all the transformations has been applied.
    vec4 finalTransformation;

    //This matrix holds the scaling matrix.
    mat4 scale = mat4(scale.x, 0, 0, 0, 0, scale.y, 0, 0, 0, 0, scale.z, 0, 0, 0, 0, 1);
    // This matrix holds the rotational matrix along x axis.
    mat4 rx = mat4(1.0, 0.0, 0.0, 0.0, 0.0, cosTheta.x, sinTheta.x, 0, 0.0, -sinTheta.x, cosTheta.x, 0, 0.0, 0.0, 0.0, 1.0);
    // This matrix holds the rotational matrix along z axis.
    mat4 rz = mat4(cosTheta.z, sinTheta.z, 0, 0, -sinTheta.z, cosTheta.z, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
    // This matrix holds the rotational matrix along y axis.
    mat4 ry = mat4(cosTheta.y, 0, -sinTheta.y, 0, 0, 1, 0, 0, sinTheta.y, 0, cosTheta.y, 0, 0, 0, 0, 1);
    // This is a matrix that holds the translation details for projection
    mat4 t = mat4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, translate.x, translate.y, translate.z, 1);
    finalTransformation = t * rx *ry * rz * scale * vPosition;

    vec3 n = normalize(eye-look), u = normalize(cross(up,n)), v = normalize(cross(n,u));

    mat4 view = mat4(u.x, v.x, n.x, 0, u.y, v.y, n.y, 0, u.z, v.z, n.z, 0, dot(-u, eye), dot(-v,eye), dot(-n,eye), 1);
    finalTransformation = view * finalTransformation;

    mat4 mat;
    switch(typeOfProjection)
    {
        case 1:  mat = getFrust();
    			break;
    	case 2:  mat = getOrtho();
    			break;
    	default: break;
    }
    finalTransformation = mat * finalTransformation;
	gl_Position =  finalTransformation;
}

/**
 *  This is a method to get the frustum or perspective projection matrix
 */
mat4 getFrust(){

 	mat4 frust = mat4(2*near/(right-left),0,0,0,
    	                  0,2*near/(top-bottom),0,0,
    	                  (right + left)/(right-left), (top+bottom)/(top-bottom),
    	                  -(far+near)/(far-near), -1,
    	                  0,0,-2*far*near/(far-near),0);
   	return frust;
}

/**
 * This is a method to get the orthogonal projection matrix
 */
mat4 getOrtho(){
	mat4 ortho = mat4(2/(right-left),0,0,0,
	    	              0, 2/(top-bottom),0,0,
	    	              0,0, -2/(far-near),0,
	    	              -(right+left)/(right-left), -(top + bottom)/(top-bottom),
	    	              -(far+near)/(far-near),1);
	return ortho;
}
