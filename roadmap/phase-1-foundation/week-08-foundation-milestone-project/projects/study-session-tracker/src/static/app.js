const subjectForm = document.getElementById("subjectForm");
const sessionForm = document.getElementById("sessionForm");
const subjectSelect = document.getElementById("subjectSelect");
const subjectsList = document.getElementById("subjectsList");
const sessionsList = document.getElementById("sessionsList");
const summaryCards = document.getElementById("summaryCards");
const messageBox = document.getElementById("messageBox");

function showMessage(text, type = "success") {
  messageBox.textContent = text;
  messageBox.className = `message ${type}`;
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const payload = await response.json();

  if (!response.ok) {
    const details = payload.details?.length ? ` ${payload.details.join(", ")}` : "";
    throw new Error(`${payload.message}${details}`);
  }

  return payload;
}

function renderSummary(summary) {
  const cards = [
    { label: "Subjects", value: summary.subject_count },
    { label: "Sessions", value: summary.total_sessions },
    { label: "Minutes", value: summary.total_minutes },
  ];

  const perSubjectCards = summary.minutes_by_subject.map((item) => ({
    label: `${item.subject_name} minutes`,
    value: item.total_minutes,
  }));

  summaryCards.innerHTML = [...cards, ...perSubjectCards]
    .map(
      (card) => `
        <article class="card summary-card">
          <p class="card-title">${card.label}</p>
          <p class="card-value">${card.value}</p>
        </article>
      `,
    )
    .join("");
}

function renderSubjects(subjects) {
  if (subjects.length === 0) {
    subjectsList.innerHTML = `<div class="card">No subjects yet. Create your first one.</div>`;
    subjectSelect.innerHTML = `<option value="">Create a subject first</option>`;
    return;
  }

  subjectsList.innerHTML = subjects
    .map(
      (subject) => `
        <article class="card">
          <strong>${subject.name}</strong>
          <p class="subject-meta">
            Category: ${subject.category} · Weekly target: ${subject.target_minutes_per_week} minutes
          </p>
        </article>
      `,
    )
    .join("");

  subjectSelect.innerHTML = subjects
    .map((subject) => `<option value="${subject.id}">${subject.name}</option>`)
    .join("");
}

function renderSessions(sessions) {
  if (sessions.length === 0) {
    sessionsList.innerHTML = `<div class="card">No sessions logged yet.</div>`;
    return;
  }

  sessionsList.innerHTML = sessions
    .map(
      (session) => `
        <article class="card">
          <strong>${session.subject_name}</strong>
          <p class="session-meta">
            ${session.session_date} · ${session.duration_minutes} minutes · Focus ${session.focus_score}/5
          </p>
          <p>${session.notes || "No notes provided."}</p>
          <div class="row-actions">
            <button class="secondary" data-delete-id="${session.id}">Delete Session</button>
          </div>
        </article>
      `,
    )
    .join("");

  document.querySelectorAll("[data-delete-id]").forEach((button) => {
    button.addEventListener("click", async () => {
      try {
        await requestJson(`/api/sessions/${button.dataset.deleteId}`, {
          method: "DELETE",
        });
        showMessage("Session deleted.");
        await loadAllData();
      } catch (error) {
        showMessage(error.message, "error");
      }
    });
  });
}

async function loadAllData() {
  const [subjectsPayload, sessionsPayload, summaryPayload] = await Promise.all([
    requestJson("/api/subjects"),
    requestJson("/api/sessions"),
    requestJson("/api/summary"),
  ]);

  renderSubjects(subjectsPayload.data);
  renderSessions(sessionsPayload.data);
  renderSummary(summaryPayload.data);
}

subjectForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(subjectForm);
  const payload = {
    name: formData.get("name"),
    category: formData.get("category"),
    target_minutes_per_week: Number(formData.get("target_minutes_per_week")),
  };

  try {
    await requestJson("/api/subjects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    subjectForm.reset();
    showMessage("Subject created.");
    await loadAllData();
  } catch (error) {
    showMessage(error.message, "error");
  }
});

sessionForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(sessionForm);
  const payload = {
    subject_id: Number(formData.get("subject_id")),
    session_date: formData.get("session_date"),
    duration_minutes: Number(formData.get("duration_minutes")),
    focus_score: Number(formData.get("focus_score")),
    notes: formData.get("notes"),
  };

  try {
    await requestJson("/api/sessions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    sessionForm.reset();
    showMessage("Study session logged.");
    await loadAllData();
  } catch (error) {
    showMessage(error.message, "error");
  }
});

loadAllData().catch((error) => {
  showMessage(error.message, "error");
});
