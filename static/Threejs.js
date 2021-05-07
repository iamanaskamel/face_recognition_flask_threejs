			function init() {
			//creating camera,scene, renderer

				camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
				camera.position.z = 400;

				scene = new THREE.Scene();
				scene.background = new THREE.Color( "#ffffff" );
                //creating mask(texture)
				var texture = new THREE.TextureLoader().load( 'static/face.png' );
                //creating box(material,geometry,mesh)
				const geometry = new THREE.BoxGeometry( 100, 100 );
				const material = new THREE.MeshBasicMaterial( { map: texture } );

				mesh = new THREE.Mesh( geometry, material );
				scene.add( mesh );

				renderer = new THREE.WebGLRenderer( { antialias: true } );
				renderer.setPixelRatio( window.devicePixelRatio );
				renderer.setSize( window.innerWidth, window.innerHeight );
				document.body.appendChild( renderer.domElement );
				document.addEventListener('mousemove', onMouseMove, false);

			}
			//to move the make ( it will be edited to coordinate of face recognition algorithm)
			function onMouseMove(event) {
                mouseX = event.clientX - window.innerWidth / 2;
                mouseY = event.clientY - window.innerHeight / 2;
                mesh.position.set(mouseX, mouseY, 0);
                //set up camera position
                camera.lookAt(scene.position);
            };

			function animate() {

				requestAnimationFrame( animate );
				renderer.render( scene, camera );

			}
			//inilizing
			init();
			animate();
