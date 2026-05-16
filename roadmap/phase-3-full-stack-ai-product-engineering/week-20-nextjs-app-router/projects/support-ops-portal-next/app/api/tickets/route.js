import { filterTickets, getAllTickets, normalizeTicketFilters } from "../../../lib/data";

export async function GET(request) {
  const { searchParams } = new URL(request.url);

  const filters = normalizeTicketFilters({
    q: searchParams.get("q") ?? "",
    status: searchParams.get("status") ?? "all",
    priority: searchParams.get("priority") ?? "all",
  });

  const items = filterTickets(getAllTickets(), filters);

  return Response.json({
    items,
    total: items.length,
    filters,
  });
}
