import Link from "next/link";

const navItems = [
  { href: "/", label: "Dashboard" },
  { href: "/tickets", label: "Tickets" },
  { href: "/compose", label: "Intake Preview" },
  { href: "/api/tickets", label: "API Example" },
];

export default function TopNav() {
  return (
    <nav className="top-nav" aria-label="Primary navigation">
      {navItems.map((item) => (
        <Link href={item.href} key={item.href}>
          {item.label}
        </Link>
      ))}
    </nav>
  );
}
