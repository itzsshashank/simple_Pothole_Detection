// document.getElementById('imageUpload').addEventListener('change', function() {
//     var file = this.files[0];
//     var imageType = /image.*/;

//     if (file.type.match(imageType)) {
//         var reader = new FileReader();

//         reader.onload = function(e) {
//             var img = new Image();
//             img.src = reader.result;

//             document.getElementById('imagePreview').innerHTML = '';
//             document.getElementById('imagePreview').appendChild(img);
//         }

//         reader.readAsDataURL(file);
//     } else {
//         alert('File not supported');
//     }
// });

// document.getElementById('uploadForm').addEventListener('submit', function(e) {
//     e.preventDefault();

//     var formData = new FormData(this);

//     fetch('/predict', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('predictionResult').innerHTML = 'Prediction: ' + data.result;
//     })
//     .catch(error => console.error('Error:', error));
// });
// Set up scene, camera, and renderer
