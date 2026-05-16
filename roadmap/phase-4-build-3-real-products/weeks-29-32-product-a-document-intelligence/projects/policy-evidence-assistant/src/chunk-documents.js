export function chunkDocuments(documents) {
  return documents.flatMap((document) => {
    const sections = document.body
      .split(/\n## /)
      .map((section, index) => (index === 0 ? section.replace(/^## /, "") : section))
      .filter(Boolean);

    return sections.map((section, sectionIndex) => {
      const [headingLine, ...rest] = section.split(/\r?\n/);
      const text = rest.join(" ").trim();

      return {
        chunkId: `${document.id}::${sectionIndex + 1}`,
        documentId: document.id,
        title: document.title,
        category: document.category,
        audience: document.audience,
        heading: headingLine.trim(),
        text,
      };
    });
  });
}
