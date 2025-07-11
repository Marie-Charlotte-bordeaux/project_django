// console.log("✅ Le fichier feedback.js est bien chargé !");

// // Vérifie que les variables globales sont bien définies
// console.log("JOB_ID:", window.JOB_ID);
// console.log("API_TOKEN:", window.API_TOKEN);
// // const token = document.querySelector('meta[name="api-token"]').getAttribute('content');
// // const token = 'eefb1fdb5e09fbde8406305956cd3799d30c2307';

// fetch('/api/feedbacks/', {
//   headers: {
//     'Authorization': 'Token ' + token
//   }
// })
// .then(res => {
//   if (!res.ok) throw new Error("Erreur " + res.status);
//   return res.json();
// })
// .then(data => {
//   console.log(data);
// })
//   .catch(err => console.error(err));

// fetch(`/api/feedbacks/?job=${window.JOB_ID}`, {
//   headers: {
//     'Authorization': 'Token ' + window.API_TOKEN
//   }
// })
// .then(res => {
//   if (!res.ok) {
//     throw new Error(`HTTP error! status: ${res.status}`);
//   }
//   return res.json();
// })
// .then(data => {
//   console.log("✅ Données feedback reçues :", data);

//   const container = document.getElementById('feedback-list');
//   container.innerHTML = '';

//   if (data.length === 0) {
//     container.innerHTML = '<p class="text-red-400">Aucun feedback trouvé.</p>';
//   }

//   data.forEach(feedback => {
//     container.innerHTML += `
//       <div class="bg-gray-800 p-4 rounded-lg shadow border-l-4 border-pink-400 mb-4">
//         <p class="font-semibold text-pink-200">${feedback.author_name}</p>
//         <p class="text-yellow-400">⭐ Note : ${feedback.rating}/5</p>
//         <p class="text-gray-300 italic">${feedback.comment}</p>
//         <small class="text-gray-500">${feedback.created_at}</small>
//       </div>
//     `;
//   });
// })
// .catch(err => console.error("❌ Erreur lors du fetch :", err));
