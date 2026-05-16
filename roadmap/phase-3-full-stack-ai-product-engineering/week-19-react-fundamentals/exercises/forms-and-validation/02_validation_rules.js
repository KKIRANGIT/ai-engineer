function validateDraft(draft) {
  const errors = {};

  if (draft.title.trim().length < 5) {
    errors.title = "Use a title with at least 5 characters.";
  }

  if (draft.description.trim().length < 20) {
    errors.description = "Add enough detail so another person can act on it.";
  }

  return errors;
}

const draft = {
  title: "Bug",
  description: "Still too short.",
};

console.log(validateDraft(draft));

/*
Notice the separation:

- validation is a pure function
- UI code decides when to show the errors
- this makes validation easier to test and reason about
*/
