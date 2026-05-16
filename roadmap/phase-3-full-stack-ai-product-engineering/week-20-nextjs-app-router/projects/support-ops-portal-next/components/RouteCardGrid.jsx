import Link from "next/link";

const cards = [
  {
    title: "Tickets route",
    href: "/tickets",
    description:
      "A server-rendered page that reads URL search params and composes the list from server data.",
  },
  {
    title: "Dynamic ticket detail",
    href: "/tickets/T-3002",
    description:
      "A route segment that resolves one ticket by id and triggers not-found behavior when needed.",
  },
  {
    title: "Intake preview",
    href: "/compose",
    description:
      "A server-rendered page with one client-side form island that talks to a route handler.",
  },
  {
    title: "API route example",
    href: "/api/tickets",
    description:
      "A route handler that returns JSON for list data and demonstrates server-side request logic.",
  },
];

export default function RouteCardGrid() {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Route map</h2>
        <p>The app is organized by route responsibilities instead of one giant frontend tree.</p>
      </div>

      <div className="route-grid">
        {cards.map((card) => (
          <Link className="route-card" href={card.href} key={card.href}>
            <h3>{card.title}</h3>
            <p>{card.description}</p>
          </Link>
        ))}
      </div>
    </section>
  );
}
