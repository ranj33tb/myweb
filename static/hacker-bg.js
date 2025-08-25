import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.154.0/build/three.module.js";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg"), alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);

// Starfield
function createStar() {
  const geometry = new THREE.SphereGeometry(0.05, 24, 24);
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
  const star = new THREE.Mesh(geometry, material);
  const [x, y, z] = Array(3).fill().map(() => THREE.MathUtils.randFloatSpread(200));
  star.position.set(x, y, z);
  scene.add(star);
}
Array(600).fill().forEach(createStar);

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);
  scene.rotation.y += 0.0005;
  renderer.render(scene, camera);
}
animate();
