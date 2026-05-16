import "./globals.css";
import TopNav from "../components/TopNav";

export const metadata = {
  title: "Support Ops Portal Next",
  description: "A Week 20 Next.js App Router learning workspace.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="site-shell">
          <header className="site-header">
            <div className="site-header__meta">
              <p className="eyebrow">Week 20 · Next.js App Router</p>
              <TopNav />
            </div>
            <div>
              <h1>Support Ops Portal</h1>
              <p>
                A server-first product shell that demonstrates layouts, route segments,
                client islands, route handlers, and streaming-friendly rendering.
              </p>
            </div>
          </header>
          {children}
        </div>
      </body>
    </html>
  );
}
