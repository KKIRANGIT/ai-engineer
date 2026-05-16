/*
This file is intentionally a teaching snippet rather than a runnable React module.

It captures the correct idea:

Use an effect when you need to synchronize React state with something outside React,
such as browser storage.
*/

import { useEffect } from "react";

function usePersistedDraft(draft) {
  useEffect(() => {
    localStorage.setItem("week-19-draft", JSON.stringify(draft));
  }, [draft]);
}

export { usePersistedDraft };

/*
Why this is a good use of an effect:

- localStorage is outside React
- the effect runs after render to sync external state

Why filtered lists do not need an effect:

- filtered lists can be computed during render from existing state
*/
