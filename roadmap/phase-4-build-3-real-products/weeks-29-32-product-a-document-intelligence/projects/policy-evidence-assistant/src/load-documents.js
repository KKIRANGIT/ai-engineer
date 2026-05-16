import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";

function parseFrontmatter(content) {
  const lines = content.split(/\r?\n/);

  if (lines[0] !== "---") {
    throw new Error("Document is missing frontmatter");
  }

  const metadata = {};
  let index = 1;

  for (; index < lines.length; index += 1) {
    const line = lines[index];

    if (line === "---") {
      index += 1;
      break;
    }

    const [key, ...rest] = line.split(":");
    metadata[key.trim()] = rest.join(":").trim();
  }

  return {
    metadata,
    body: lines.slice(index).join("\n").trim(),
  };
}

export function loadDocuments(documentsDir) {
  const filenames = readdirSync(documentsDir).filter((name) => name.endsWith(".md"));

  return filenames.map((filename) => {
    const fullPath = path.join(documentsDir, filename);
    const content = readFileSync(fullPath, "utf8");
    const { metadata, body } = parseFrontmatter(content);

    return {
      ...metadata,
      body,
      sourcePath: fullPath,
    };
  });
}
