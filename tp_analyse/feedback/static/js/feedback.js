document.addEventListener("DOMContentLoaded", function () {
  const jobId = window.JOB_ID;
  const container = document.getElementById("feedback-list");

  function renderFeedback(feedback) {
    return `
      <div class="bg-gray-800 p-4 rounded-lg shadow border-l-4 border-pink-400">
        <p class="font-semibold text-pink-200">${feedback.author_name}</p>
        <p class="text-yellow-400">⭐ Note : ${feedback.rating}/5</p>
        <p class="text-gray-300 italic">${feedback.comment}</p>
        <small class="text-gray-500">${new Date(feedback.created_at).toLocaleString()}</small>
      </div>
    `;
  }

  function loadFeedbacks() {
    fetch(`/api/feedbacks/?job=${jobId}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.length === 0) {
          container.innerHTML = `<p class="text-red-400">Aucun feedback trouvé.</p>`;
        } else {
          container.innerHTML = data.map(renderFeedback).join("");
        }
      })
      .catch((err) => {
        console.error("Erreur chargement feedbacks", err);
        container.innerHTML = `<p class="text-red-500">Erreur de chargement des feedbacks.</p>`;
      });
  }

  loadFeedbacks(); // au chargement

  // On exporte la fonction si besoin plus tard
  window.loadFeedbacks = loadFeedbacks;
});

const form = document.querySelector("form");
if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = {
      job: window.JOB_ID,
      author_name: formData.get("author_name"),
      rating: parseInt(formData.get("rating")),
      comment: formData.get("comment")
    };

    fetch("/api/feedbacks/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
      },
      body: JSON.stringify(data)
    })
      .then((res) => {
        if (!res.ok) throw new Error("Erreur réseau");
        return res.json();
      })
      .then((data) => {
        alert("Feedback ajouté !");
        if (window.loadFeedbacks) window.loadFeedbacks(); // recharge la liste
        form.reset(); // vide le formulaire
      })
      .catch((err) => {
        console.error(err);
        alert("Erreur lors de l'envoi du feedback.");
      });
  });
}

// Fonction utilitaire pour le token CSRF
function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}
