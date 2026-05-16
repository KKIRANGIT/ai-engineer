import { formatCreatedDate } from "../utils.js";

function ActivityFeed({ activities }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Recent activity</h2>
        <p>A derived view built from the same ticket data.</p>
      </div>

      <ul className="activity-list">
        {activities.map((activity) => (
          <li className="activity-item" key={activity.id}>
            <div>
              <strong>{activity.title}</strong>
              <p>{activity.message}</p>
            </div>
            <div className="activity-item__meta">
              <span>{activity.meta}</span>
              <span>{formatCreatedDate(activity.createdAt)}</span>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default ActivityFeed;
