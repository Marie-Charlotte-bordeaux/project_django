// ✅ Quand le DOM est chargé :
document.addEventListener("DOMContentLoaded", function () {
  const jobId = window.JOB_ID; // ID du job passé depuis Django
  const container = document.getElementById("feedback-list"); // div pour afficher les feedbacks
  console.log("🎉 Script feedback.js chargé !");
  console.log("✅ TOKEN utilisé :", window.API_TOKEN);

  // ------------------------------------------------------------------------
  // ✅ 1) Fonction pour charger les feedbacks (GET)
  // ------------------------------------------------------------------------
  function loadFeedbacks() {
    console.log("🔄 Chargement des feedbacks...");

    fetch(`/api/feedbacks/?job=${jobId}`, {
      headers: {
        Authorization: "Token " + window.API_TOKEN, // Token DRF 
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("📥 Données reçues :", data);

        if (!Array.isArray(data)) {
          console.error("❌ Réponse inattendue :", data);
          container.innerHTML = `<p class="text-red-500">Réponse inattendue du serveur.</p>`;
          return;
        }

        if (data.length === 0) {
          container.innerHTML = `<p class="text-red-400">Aucun feedback trouvé.</p>`;
        } else {
          container.innerHTML = data.map(renderFeedback).join("");
        }
      })
      .catch((err) => {
        console.error("❌ Erreur chargement feedbacks :", err);
        container.innerHTML = `<p class="text-red-500">Erreur de chargement des feedbacks.</p>`;
      });
  }

  // Lance le chargement au démarrage
  loadFeedbacks();
  window.loadFeedbacks = loadFeedbacks; // Exporte pour réutiliser après un POST

  // ------------------------------------------------------------------------
  // ✅ 2) Gestion du formulaire « Ajouter un feedback » (POST)
  // ------------------------------------------------------------------------
  const form = document.querySelector("form[method='post']"); 
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // Empêche le submit HTML classique

      const formData = new FormData(form); // Récupère les champs du form
      const data = {
        job: jobId,
        author_name: formData.get("author_name"),
        rating: parseInt(formData.get("rating")),
        comment: formData.get("comment"),
      };

      console.log("📤 Données envoyées :", data);

      fetch("/api/feedbacks/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + window.API_TOKEN, // Token DRF 
        },
        body: JSON.stringify(data),
      })
        .then((res) => {
          if (!res.ok) throw new Error("Erreur réseau : " + res.status);
          return res.json();
        })
        .then((data) => {
          console.log("✅ Feedback ajouté :", data);
          alert("Feedback ajouté !");
          loadFeedbacks(); // Recharge la liste après ajout
          form.reset(); // Réinitialise le form
        })
        .catch((err) => {
          console.error("❌ Erreur lors de l'envoi :", err);
          alert("Erreur lors de l'envoi du feedback.");
        });
    });
  } else {
    console.warn("⚠️ Aucun formulaire d'ajout trouvé. Vérifie ton HTML !");
  }

  // ------------------------------------------------------------------------
  // ✅ 3) Gestion du filtre « min_rating » (faire un filtrage JS)
  // ------------------------------------------------------------------------
  const filterForm = document.querySelector("form[method='get']");
  const minRatingInput = document.getElementById("min_rating");

  if (filterForm) {
    filterForm.addEventListener("submit", function (e) {
      e.preventDefault(); // Empêche le reload+
      const jobId = window.JOB_ID;
      const minRating = document.getElementById("min_rating").value;
      let url = `/api/feedbacks/?job=${jobId}`;
      if (minRating) {
        url += `&rating=${minRating}`;
      }

      console.log("🔎 Filtre URL :", url);

      fetch(url, {
        headers: {
          Authorization: "Token " + window.API_TOKEN,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("📥 Résultat filtre :", data);

          if (!Array.isArray(data)) {
            container.innerHTML = "<p>Réponse inattendue du serveur.</p>";
            return;
          }
          if (data.length === 0) {
            container.innerHTML = "<p>Aucun feedback pour ce filtre.</p>";
            return;
          }

          container.innerHTML = data.map(renderFeedback).join("");
        })
        .catch((err) => {
          console.error("❌ Erreur filtre :", err);
          container.innerHTML = "<p>Erreur lors du filtrage.</p>";
        });
    });
  }

  // ------------------------------------------------------------------------
  // ✅ 4) Fonction utilitaire pour afficher 1 feedback
  // ------------------------------------------------------------------------
  function renderFeedback(feedback) {
    return `
      <div class="bg-gray-800 p-4 rounded-lg shadow border-l-4 border-pink-400 mb-2">
        <p class="font-semibold text-pink-200">Candidate : ${feedback.author_name}</p>
        <p class="text-yellow-400">⭐ Note : ${feedback.rating}/5</p>
        <p class="text-gray-300 italic">${feedback.comment}</p>
        <small class="text-gray-500">${new Date(feedback.created_at).toLocaleString()}</small>
      </div>
    `;
  }
});
