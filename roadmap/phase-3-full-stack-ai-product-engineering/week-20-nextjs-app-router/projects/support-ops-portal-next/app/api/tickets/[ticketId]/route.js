import { getTicketById } from "../../../../lib/data";

export async function GET(_request, { params }) {
  const { ticketId } = await params;
  const ticket = getTicketById(ticketId);

  if (!ticket) {
    return Response.json(
      {
        error: `Ticket ${ticketId} was not found.`,
      },
      { status: 404 },
    );
  }

  return Response.json(ticket);
}
