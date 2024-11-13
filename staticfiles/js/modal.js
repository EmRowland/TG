// const readMoreButtons = document.querySelectorAll('.read-more-button');
// const modal = document.querySelector('.modal');
// const modalTitle = document.getElementById('modal-title');
// const modalContent = document.getElementById('modal-content');
// const closeButton = document.querySelector('.close-button');








// const my_event = document.getElementById('myEvent');

// function myEvent() {
//     my_event.forEach(button => {
//         button.addEventListener('click', () => {
//             fetch(`/get_post/${postId}`)
//                 .then(response => response.json())
//                 .then(data => {
//                     modalTitle.textContent = data.title;
//                     modalContent.textContent = data.content;
//                     modal.style.display = 'block';
//                 });

//         });
        


//     });
// }









// function myfunc() {
//     readMoreButtons.forEach(button => {
//         button.addEventListener('click', () => {
//             const postId = button.getAttribute('data-event-id');

//             // Use Ajax to fetch the full content of the blog post based on postId
//             // Replace this with your actual Ajax code
//             // For example:
//             fetch(`/get_post/${postId}`)
//                 .then(response => response.json())
//                 .then(data => {
//                     modalTitle.textContent = data.title;
//                     modalContent.textContent = data.content;
//                     modal.style.display = 'block';
//                 });
//         });
//     });

//     closeButton.addEventListener('click', () => {
//         modal.style.display = 'none';
//     });

//     window.addEventListener('click', (event) => {
//         if (event.target === modal) {
//             modal.style.display = 'none';
//         }
//     });





// }
// readMoreButtons.forEach(button => {
//     button.addEventListener('click', () => {
//         const postId = button.getAttribute('data-post-id');

//         // Use Ajax to fetch the full content of the blog post based on postId
//         // Replace this with your actual Ajax code
//         // For example:
//         fetch(`/get_post/${postId}`)
//             .then(response => response.json())
//             .then(data => {
//                 modalTitle.textContent = data.title;
//                 modalContent.textContent = data.content;
//                 modal.style.display = 'block';
//             });
//     });
// });

// closeButton.addEventListener('click', () => {
//     modal.style.display = 'none';
// });

// window.addEventListener('click', (event) => {
//     if (event.target === modal) {
//         modal.style.display = 'none';
//     }
// });