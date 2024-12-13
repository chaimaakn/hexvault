import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import Countries from '../assets/custom.geo.json'; // Assuming you imported as Countries

const ShaderSphere = () => {
  const mountRef = useRef(null);

  useEffect(() => {
    const vertexShader = `
      uniform float u_time;
      uniform float u_maxExtrusion;

      void main() {
        vec3 newPosition = position;
        if (u_maxExtrusion > 1.0) {
          newPosition.xyz = newPosition.xyz * u_maxExtrusion + sin(u_time);
        } else {
          newPosition.xyz = newPosition.xyz * u_maxExtrusion;
        }
        gl_Position = projectionMatrix * modelViewMatrix * vec4(newPosition, 1.0);
      }
    `;

    const fragmentShader = `
      uniform float u_time;
      vec3 colorA = vec3(0.0235, 0.2509, 0.1686); 
      void main() {
        gl_FragColor = vec4(colorA, 0.9); 
      }
    `;

    // Scene setup
    const scene = new THREE.Scene();

    // Camera setup
    const sizes = { width: window.innerWidth / 2, height: window.innerHeight };
    const camera = new THREE.PerspectiveCamera(30, sizes.width / sizes.height, 1, 1000);
    camera.position.x = 100;
    camera.position.y = 0;
    camera.position.z = 0;
    camera.updateProjectionMatrix();

    // Lighting setup
    const dlight = new THREE.DirectionalLight(0xffffff, 0.8);
    dlight.position.set(100, 2000, 400);
    camera.add(dlight);

    const dlight1 = new THREE.DirectionalLight(0x7982f6, 1);
    dlight1.position.set(-200, 500, 200);
    camera.add(dlight1);

    const dlight2 = new THREE.PointLight(0x8566cc, 0.8);
    dlight2.position.set(-200, 500, 200);
    camera.add(dlight2);

    scene.add(camera);
    scene.fog = new THREE.Fog(0xffffff, 400, 2000);

    // Renderer setup
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(sizes.width, sizes.height);
    renderer.setPixelRatio(window.devicePixelRatio);
    mountRef.current.appendChild(renderer.domElement);

    // Controls setup
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.autoRotate = true;
    controls.autoRotateSpeed = 1.2;
    controls.enableDamping = true;

    // Ambient light
    const ambientlight = new THREE.AmbientLight(0xbbbbbb, 0.3);
    scene.add(ambientlight);

    // Sphere geometry and material
    const sphereGeometry = new THREE.SphereGeometry(19.5, 35, 35);
    const shaderMaterial = new THREE.ShaderMaterial({
      vertexShader,
      fragmentShader,
      uniforms: {
        u_time: { value: 1.0 },
        u_maxExtrusion: { value: 1.0 },
      },
      side: THREE.DoubleSide,
    });
    const sphere = new THREE.Mesh(sphereGeometry, shaderMaterial);
    scene.add(sphere);

    

    // Animation loop
    const clock = new THREE.Clock();
    const animate = () => {
      requestAnimationFrame(animate);
      shaderMaterial.uniforms.u_time.value += clock.getDelta();
      controls.update();
      renderer.render(scene, camera);
    };

    animate();

    // Handle resize
    const handleResize = () => {
      sizes.width = window.innerWidth/2;
      sizes.height = window.innerHeight;
      camera.aspect = sizes.width / sizes.height;
      camera.updateProjectionMatrix();
      renderer.setSize(sizes.width, sizes.height);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      mountRef.current.removeChild(renderer.domElement);
    };
  }, []);

  return <div ref={mountRef} style={{
    width: '100%',
    height: '100%',
    position: 'relative',
    overflow: 'hidden', // Prevent overflowing of the globe
  }} />;
};

export default ShaderSphere;
