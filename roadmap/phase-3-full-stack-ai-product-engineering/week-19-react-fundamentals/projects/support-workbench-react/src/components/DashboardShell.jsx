function DashboardShell({ title, subtitle, children }) {
  return (
    <div className="page-shell">
      <header className="page-header">
        <p className="eyebrow">Week 19 · React Fundamentals</p>
        <h1>{title}</h1>
        <p className="page-subtitle">{subtitle}</p>
      </header>
      <main>{children}</main>
    </div>
  );
}

export default DashboardShell;
