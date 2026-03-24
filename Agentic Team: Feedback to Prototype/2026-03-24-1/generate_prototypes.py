#!/usr/bin/env python3
import os

# Define the remaining prototypes with their unique content
prototypes = {
    "o9-us1": {
        "title": "Quick Add via Search with Typeahead",
        "section": "Group Participant Addition",
        "content": """
        <div class="content-label">Group Chat</div>

        <div class="hero-banner">
          <div class="hero-title">Add Members to Team Discussion</div>
          <div class="hero-subtitle">Quickly find and add team members to this group chat.</div>
        </div>

        <div class="content-section">
          <div class="section-title">
            <span class="section-title-icon">➕</span>
            Search for Members
          </div>
          <input type="text" class="search-input" placeholder="Start typing a name or email..." onkeyup="filterMembers(this.value)">

          <div id="memberList" class="member-list" style="margin-top: 16px;">
            <div class="member-item" data-search="marie laurent">
              <div class="member-avatar">ML</div>
              <div class="member-info">
                <div class="member-name">Dr. Marie Laurent</div>
                <div class="member-email">marie.laurent@hopital.fr</div>
              </div>
              <button class="member-btn">Add</button>
            </div>
            <div class="member-item" data-search="pierre dubois">
              <div class="member-avatar">PD</div>
              <div class="member-info">
                <div class="member-name">Dr. Pierre Dubois</div>
                <div class="member-email">p.dubois@clinic.com</div>
              </div>
              <button class="member-btn">Add</button>
            </div>
            <div class="member-item" data-search="sophie martin">
              <div class="member-avatar">SM</div>
              <div class="member-info">
                <div class="member-name">Dr. Sophie Martin</div>
                <div class="member-email">sophie.m@hopital.fr</div>
              </div>
              <button class="member-btn">Add</button>
            </div>
            <div class="member-item" data-search="james wilson">
              <div class="member-avatar">JW</div>
              <div class="member-info">
                <div class="member-name">Dr. James Wilson</div>
                <div class="member-email">j.wilson@clinic.uk</div>
              </div>
              <button class="member-btn">Add</button>
            </div>
          </div>
        </div>

        <div class="content-section">
          <div class="section-title">
            <span class="section-title-icon">✓</span>
            Current Members (3)
          </div>
          <div class="member-list" style="margin-top: 12px;">
            <div class="member-item">
              <div class="member-avatar" style="background: #00C48C;">AM</div>
              <div class="member-info">
                <div class="member-name">Dr. Anna Mueller</div>
                <div class="member-email">anna.mueller@hopital.de</div>
              </div>
              <div style="font-size: 12px; color: #00C48C;">Added</div>
            </div>
            <div class="member-item">
              <div class="member-avatar" style="background: #00C48C;">TK</div>
              <div class="member-info">
                <div class="member-name">Dr. Tomas Kovács</div>
                <div class="member-email">t.kovacs@hopital.hu</div>
              </div>
              <div style="font-size: 12px; color: #00C48C;">Added</div>
            </div>
            <div class="member-item">
              <div class="member-avatar" style="background: #00C48C;">LC</div>
              <div class="member-info">
                <div class="member-name">Dr. Lisa Chen</div>
                <div class="member-email">lisa.chen@clinic.cn</div>
              </div>
              <div style="font-size: 12px; color: #00C48C;">Added</div>
            </div>
          </div>
        </div>

        <div class="button-group">
          <button class="btn btn-primary">Done</button>
          <button class="btn btn-secondary">Cancel</button>
        </div>

        <script>
          function filterMembers(query) {
            const items = document.querySelectorAll('.member-item');
            items.forEach(item => {
              const searchText = item.getAttribute('data-search') || '';
              if (searchText.includes(query.toLowerCase())) {
                item.style.display = 'flex';
              } else if (query.length > 0) {
                item.style.display = 'none';
              } else {
                item.style.display = 'flex';
              }
            });
          }
        </script>
        """
    },
    "o4-us1": {
        "title": "Optimistic UI Updates with Fallback",
        "section": "Conversation Lag & Sync",
        "content": """
        <div class="content-label">Messaging</div>

        <div class="hero-banner">
          <div class="hero-title">Team Discussion — Cardiology Consult</div>
          <div class="hero-subtitle">Real-time conversation with optimistic message delivery.</div>
        </div>

        <div class="content-section">
          <div class="message-thread" style="max-height: 400px; overflow-y: auto; margin-bottom: 16px;">
            <div class="message sent">
              <div class="message-content">
                <div class="message-text">Patient referral approved for Tuesday</div>
                <div class="message-time">11:32 AM</div>
              </div>
            </div>
            <div class="message received">
              <div class="message-content">
                <div class="message-text">Perfect. I'll schedule the appointment slot.</div>
                <div class="message-time">11:33 AM</div>
              </div>
            </div>
            <div class="message sent optimistic">
              <div class="message-content">
                <div class="message-text">Let me know once it's confirmed</div>
                <div class="message-time">Sending...</div>
              </div>
            </div>
            <div class="message received">
              <div class="message-content">
                <div class="message-text">Done! Scheduled for 2:00 PM Tuesday</div>
                <div class="message-time">11:34 AM</div>
              </div>
            </div>
          </div>
        </div>

        <div class="info-banner" style="background: #E8F4FD; border-color: #0596DE;">
          <div class="info-banner-icon">✓</div>
          <div class="info-banner-content">
            <div class="info-banner-title">Message sent immediately</div>
            <div class="info-banner-text">Your message appears right away while we sync in the background. If there's any issue, you'll see an error notification.</div>
          </div>
        </div>

        <div class="content-section">
          <div class="section-title">
            <span class="section-title-icon">💬</span>
            New Message
          </div>
          <textarea class="message-input" placeholder="Type your message here..."></textarea>
          <div class="button-group" style="margin-top: 12px;">
            <button class="btn btn-primary">Send Message</button>
          </div>
        </div>

        <style>
          .message-thread {
            background: var(--dtl-gray-50);
            border-radius: 8px;
            padding: 12px;
          }

          .message {
            display: flex;
            margin-bottom: 12px;
            animation: slideIn 0.2s ease;
          }

          @keyframes slideIn {
            from {
              opacity: 0;
              transform: translateY(10px);
            }
            to {
              opacity: 1;
              transform: translateY(0);
            }
          }

          .message.sent {
            justify-content: flex-end;
          }

          .message.received {
            justify-content: flex-start;
          }

          .message-content {
            max-width: 60%;
            padding: 10px 14px;
            border-radius: 8px;
            background: var(--dtl-blue);
            color: white;
          }

          .message.received .message-content {
            background: var(--dtl-white);
            color: var(--dtl-gray-800);
            border: 1px solid var(--dtl-gray-200);
          }

          .message-content .message-text {
            font-size: 14px;
            margin-bottom: 4px;
          }

          .message-content .message-time {
            font-size: 11px;
            opacity: 0.7;
          }

          .message.optimistic .message-content {
            opacity: 0.7;
          }

          .message-input {
            width: 100%;
            padding: 12px;
            border: 1px solid var(--dtl-gray-200);
            border-radius: 6px;
            font-family: inherit;
            font-size: 14px;
            min-height: 80px;
            resize: vertical;
          }
        </style>
        """
    },
    "o4-us4": {
        "title": "Lag Detection & User Notification",
        "section": "Conversation Lag & Sync",
        "content": """
        <div class="content-label">Messaging</div>

        <div class="hero-banner">
          <div class="hero-title">Team Discussion — Patient Care</div>
          <div class="hero-subtitle">Network synchronization in progress.</div>
        </div>

        <div class="lag-banner" style="background: #FFF3E0; border: 1px solid #FFB020; border-radius: 8px; padding: 16px; margin-bottom: 24px; display: flex; gap: 12px;">
          <div style="font-size: 20px; animation: spin 2s linear infinite;">⚠</div>
          <div>
            <div style="font-weight: 600; color: #FF9800; margin-bottom: 4px;">Network lag detected</div>
            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">Messages are taking longer to sync (2.3 seconds). Some messages may appear out of order.</div>
            <button class="btn" style="padding: 6px 12px; font-size: 12px;">Retry Connection</button>
          </div>
        </div>

        <div class="content-section">
          <div class="section-title">
            <span class="section-title-icon">💬</span>
            Messages (syncing...)
          </div>
          <div class="message-thread" style="max-height: 400px; overflow-y: auto;">
            <div class="message received">
              <div class="message-content">
                <div class="message-text">Patient transport arranged for Wednesday</div>
                <div class="message-time">11:28 AM ✓</div>
              </div>
            </div>
            <div class="message sent" style="opacity: 0.6;">
              <div class="message-content">
                <div class="message-text">Great, thanks for handling that</div>
                <div class="message-time">Pending sync...</div>
              </div>
            </div>
            <div class="message received">
              <div class="message-content">
                <div class="message-text">Need lab results before discharge</div>
                <div class="message-time">11:30 AM ✓</div>
              </div>
            </div>
          </div>
        </div>

        <div class="info-banner">
          <div class="info-banner-icon">ℹ</div>
          <div class="info-banner-content">
            <div class="info-banner-title">How lag detection works</div>
            <div class="info-banner-text">When messages take longer than 2 seconds to sync, we show this warning. You can still send messages—they'll sync automatically when your connection improves.</div>
          </div>
        </div>

        <style>
          @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
          }
          .message-thread {
            background: var(--dtl-gray-50);
            border-radius: 8px;
            padding: 12px;
          }
          .message {
            display: flex;
            margin-bottom: 12px;
          }
          .message.sent {
            justify-content: flex-end;
          }
          .message.received {
            justify-content: flex-start;
          }
          .message-content {
            max-width: 60%;
            padding: 10px 14px;
            border-radius: 8px;
            background: var(--dtl-blue);
            color: white;
          }
          .message.received .message-content {
            background: var(--dtl-white);
            color: var(--dtl-gray-800);
            border: 1px solid var(--dtl-gray-200);
          }
          .message-content .message-text {
            font-size: 14px;
            margin-bottom: 4px;
          }
          .message-content .message-time {
            font-size: 11px;
            opacity: 0.7;
          }
        </style>
        """
    }
}

# Base template HTML structure
base_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Doctolib Connect — {title}</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap');
    :root {{
      --dtl-navy: #1B2A4A;
      --dtl-navy-light: #243557;
      --dtl-blue: #0596DE;
      --dtl-blue-dark: #0080C5;
      --dtl-blue-light: #E8F4FD;
      --dtl-green: #00C48C;
      --dtl-white: #FFFFFF;
      --dtl-gray-50: #F7F8FA;
      --dtl-gray-100: #F0F2F5;
      --dtl-gray-200: #E4E7EB;
      --dtl-gray-300: #CDD1D8;
      --dtl-gray-400: #9BA3AE;
      --dtl-gray-500: #6B7280;
      --dtl-gray-600: #4B5563;
      --dtl-gray-700: #374151;
      --dtl-gray-800: #1F2937;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--dtl-gray-50); color: var(--dtl-gray-600); }}
    .page-wrapper {{ display: flex; height: 100vh; }}
    .sidebar {{ width: 76px; background: var(--dtl-navy); border-right: 1px solid rgba(0, 0, 0, 0.1); padding: 16px 0; display: flex; flex-direction: column; align-items: center; gap: 12px; }}
    .sidebar-logo {{ width: 48px; height: 48px; background: rgba(255, 255, 255, 0.1); border-radius: 6px; display: flex; align-items: center; justify-content: center; color: var(--dtl-white); font-weight: 700; font-size: 20px; margin-bottom: 8px; }}
    .sidebar-item {{ width: 52px; height: 52px; background: transparent; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: rgba(255, 255, 255, 0.6); cursor: pointer; font-size: 20px; transition: all 0.15s; }}
    .sidebar-item:hover {{ background: var(--dtl-navy-light); }}
    .sidebar-item.active {{ background: rgba(255, 255, 255, 0.1); color: var(--dtl-white); }}
    .sidebar-item.badge {{ position: relative; }}
    .sidebar-badge {{ position: absolute; top: -4px; right: -4px; background: var(--dtl-blue); color: var(--dtl-white); font-size: 9px; font-weight: 700; padding: 2px 6px; border-radius: 9999px; border: 2px solid var(--dtl-navy); }}
    .header {{ position: absolute; top: 0; left: 76px; right: 0; height: 52px; background: var(--dtl-navy); border-bottom: 1px solid rgba(0, 0, 0, 0.1); padding: 0 32px; display: flex; align-items: center; justify-content: space-between; z-index: 100; }}
    .header-left {{ display: flex; align-items: center; gap: 16px; }}
    .header-search {{ background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 6px; padding: 6px 12px; color: rgba(255, 255, 255, 0.7); font-size: 13px; width: 200px; }}
    .header-right {{ display: flex; align-items: center; gap: 12px; }}
    .header-icon {{ color: rgba(255, 255, 255, 0.6); cursor: pointer; font-size: 16px; transition: color 0.15s; }}
    .header-icon:hover {{ color: var(--dtl-white); }}
    .header-avatar {{ width: 32px; height: 32px; background: rgba(255, 255, 255, 0.2); border-radius: 6px; display: flex; align-items: center; justify-content: center; color: rgba(255, 255, 255, 0.7); font-size: 14px; }}
    .sub-sidebar {{ position: fixed; left: 76px; top: 52px; width: 230px; height: calc(100vh - 52px); background: var(--dtl-white); border-right: 1px solid var(--dtl-gray-200); padding: 24px 0; overflow-y: auto; }}
    .sub-sidebar-section {{ padding: 0 16px; margin-bottom: 24px; }}
    .sub-sidebar-label {{ font-size: 11px; font-weight: 700; color: var(--dtl-gray-400); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; padding: 0 4px; }}
    .sub-sidebar-link {{ display: block; padding: 10px 12px; border-radius: 6px; color: var(--dtl-gray-600); text-decoration: none; font-size: 14px; font-weight: 500; transition: all 0.15s; margin-bottom: 4px; }}
    .sub-sidebar-link:hover {{ background: var(--dtl-gray-50); color: var(--dtl-blue); }}
    .sub-sidebar-link.active {{ background: var(--dtl-blue-light); color: var(--dtl-blue); font-weight: 600; }}
    .main {{ margin-left: 76px; margin-top: 52px; flex: 1; display: flex; }}
    .content {{ flex: 1; background: var(--dtl-gray-50); padding: 32px; overflow-y: auto; max-height: calc(100vh - 52px); }}
    .content-inner {{ max-width: 1000px; margin: 0 auto; }}
    .content-label {{ font-size: 13px; font-weight: 700; color: var(--dtl-gray-400); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 16px; }}
    .hero-banner {{ background: var(--dtl-white); border-radius: 12px; padding: 32px; margin-bottom: 32px; box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); }}
    .hero-title {{ font-size: 24px; font-weight: 700; color: var(--dtl-gray-800); margin-bottom: 12px; }}
    .hero-subtitle {{ font-size: 15px; color: var(--dtl-gray-600); margin-bottom: 24px; }}
    .content-section {{ background: var(--dtl-white); border: 1px solid var(--dtl-gray-200); border-radius: 8px; padding: 24px; margin-bottom: 24px; }}
    .section-title {{ font-size: 16px; font-weight: 700; color: var(--dtl-gray-800); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    .section-title-icon {{ font-size: 18px; }}
    .search-input {{ width: 100%; padding: 10px 12px; border: 1px solid var(--dtl-gray-200); border-radius: 6px; font-family: inherit; font-size: 14px; margin-bottom: 12px; }}
    .member-list {{ display: flex; flex-direction: column; gap: 8px; }}
    .member-item {{ display: flex; align-items: center; gap: 12px; padding: 12px; background: var(--dtl-gray-50); border-radius: 6px; }}
    .member-avatar {{ width: 36px; height: 36px; background: var(--dtl-blue); border-radius: 6px; display: flex; align-items: center; justify-content: center; color: var(--dtl-white); font-size: 12px; font-weight: 600; flex-shrink: 0; }}
    .member-info {{ flex: 1; }}
    .member-name {{ font-weight: 600; color: var(--dtl-gray-800); font-size: 14px; }}
    .member-email {{ font-size: 12px; color: var(--dtl-gray-500); }}
    .member-btn {{ padding: 6px 12px; background: var(--dtl-blue); color: var(--dtl-white); border: none; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: 600; transition: all 0.15s; }}
    .member-btn:hover {{ background: var(--dtl-blue-dark); }}
    .info-banner {{ background: var(--dtl-blue-light); border: 1px solid var(--dtl-blue); border-radius: 8px; padding: 16px; margin-bottom: 24px; display: flex; gap: 12px; }}
    .info-banner-icon {{ color: var(--dtl-blue); font-size: 20px; flex-shrink: 0; }}
    .info-banner-content {{ flex: 1; }}
    .info-banner-title {{ font-weight: 600; color: var(--dtl-blue); margin-bottom: 4px; font-size: 14px; }}
    .info-banner-text {{ font-size: 13px; color: var(--dtl-gray-600); line-height: 1.5; }}
    .button-group {{ display: flex; gap: 12px; margin-top: 24px; }}
    .btn {{ padding: 10px 20px; border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.15s; border: none; }}
    .btn-primary {{ background: var(--dtl-blue); color: var(--dtl-white); }}
    .btn-primary:hover {{ background: var(--dtl-blue-dark); }}
    .btn-secondary {{ background: var(--dtl-white); color: var(--dtl-blue); border: 1px solid var(--dtl-blue); }}
    .btn-secondary:hover {{ background: var(--dtl-blue-light); }}
    .floating-nav {{ position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: var(--dtl-navy); border-radius: 24px; padding: 12px 24px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); display: flex; gap: 16px; align-items: center; z-index: 9999; font-family: 'Open Sans', sans-serif; font-size: 14px; font-weight: 500; }}
    .floating-nav a {{ color: rgba(255, 255, 255, 0.6); text-decoration: none; padding: 6px 12px; border-radius: 6px; transition: all 0.2s; display: flex; align-items: center; gap: 6px; }}
    .floating-nav a:hover {{ background: rgba(255, 255, 255, 0.1); color: var(--dtl-white); }}
    .floating-nav a.active {{ background: rgba(5, 150, 222, 0.3); color: #5BC0F0; }}
    .floating-nav-divider {{ width: 1px; height: 20px; background: rgba(255, 255, 255, 0.2); }}
    .floating-nav-priority {{ display: flex; align-items: center; gap: 6px; color: rgba(255, 255, 255, 0.6); }}
    .priority-dot {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #EF4444; }}
    .floating-nav-options {{ display: flex; gap: 8px; }}
  </style>
</head>
<body>
  <div class="page-wrapper">
    <div class="sidebar">
      <div class="sidebar-logo">D</div>
      <div class="sidebar-item active">📋</div>
      <div class="sidebar-item">📅</div>
      <div class="sidebar-item">✓</div>
      <div class="sidebar-item badge">
        💬
        <span class="sidebar-badge">12</span>
      </div>
      <div class="sidebar-item">✉</div>
      <div class="sidebar-item">👥</div>
      <div class="sidebar-item">📧</div>
      <div class="sidebar-item">📄</div>
      <div class="sidebar-item">💵</div>
      <div class="sidebar-item">📊</div>
    </div>
    <div class="header">
      <div class="header-left">
        <input class="header-search" placeholder="Search messages, people...">
      </div>
      <div class="header-right">
        <div class="header-icon">🔔</div>
        <div class="header-icon">⚙</div>
        <div class="header-avatar">CH</div>
      </div>
    </div>
    <div class="sub-sidebar">
      <div class="sub-sidebar-section">
        <div class="sub-sidebar-label">Connect</div>
        <a href="#" class="sub-sidebar-link">Discussions</a>
        <a href="#" class="sub-sidebar-link">Tele-expertise</a>
        <a href="#" class="sub-sidebar-link">Networks</a>
      </div>
    </div>
    <div class="main">
      <div class="content">
        <div class="content-inner">
          {content}
        </div>
      </div>
    </div>
  </div>

  <div class="floating-nav">
    <a href="../index.html">🏠 Home</a>
    <div class="floating-nav-divider"></div>
    <div class="floating-nav-priority">
      <span class="priority-dot"></span>
      {nav_priority}
    </div>
    <div class="floating-nav-options">
      {nav_options}
    </div>
  </div>
</body>
</html>'''

# Create prototypes
base_dir = "/sessions/blissful-elegant-ride/mnt/Agentic Team: Feedback to Prototype/2026-03-24-1"

# Mapping of stories to nav configurations
story_mappings = {
    "o9-us1": {
        "nav_priority": "O9",
        "nav_options": '<a href="#" class="active">US1</a>\n      <a href="../o9-us4/page.html">US4</a>\n      <a href="../o9-us2/page.html">US2</a>'
    },
    "o4-us1": {
        "nav_priority": "O4",
        "nav_options": '<a href="#" class="active">US1</a>\n      <a href="../o4-us4/page.html">US4</a>\n      <a href="../o4-us2/page.html">US2</a>\n      <a href="../o4-us3/page.html">US3</a>'
    },
    "o4-us4": {
        "nav_priority": "O4",
        "nav_options": '<a href="../o4-us1/page.html">US1</a>\n      <a href="#" class="active">US4</a>\n      <a href="../o4-us2/page.html">US2</a>\n      <a href="../o4-us3/page.html">US3</a>'
    }
}

for story_id, proto_info in prototypes.items():
    dir_path = os.path.join(base_dir, story_id)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, "page.html")
    nav_info = story_mappings.get(story_id, {"nav_priority": "O?", "nav_options": ""})

    html = base_template.format(
        title=proto_info["title"],
        content=proto_info["content"],
        nav_priority=nav_info["nav_priority"],
        nav_options=nav_info["nav_options"]
    )

    with open(file_path, 'w') as f:
        f.write(html)

    print(f"✓ Created {story_id}/page.html")

print("\nDone! Generated 3 prototypes.")
