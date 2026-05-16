import { buildIntakePreview, validateIntakeDraft } from "../../../lib/intake";

export async function POST(request) {
  const draft = await request.json();
  const errors = validateIntakeDraft(draft);

  if (Object.keys(errors).length > 0) {
    return Response.json(
      {
        ok: false,
        errors,
      },
      { status: 400 },
    );
  }

  return Response.json({
    ok: true,
    preview: buildIntakePreview(draft),
  });
}
