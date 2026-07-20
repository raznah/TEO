# Product Decisions

---

# Product Decisions

This document records product decisions that shape the user experience of TEO.

Unlike the Architecture document, these decisions describe *what* the application should do and *how it should feel* from the player's perspective.

Every significant product decision should be recorded here before implementation.

---

## PD-001

### Decision

The dashboard is composed of reusable Panels.

### Reasoning

Each widget answers a specific player question instead of simply displaying information.

### Impact

New dashboard functionality should be implemented as widgets whenever possible.

---

## PD-002

### Decision

TEO greets the player with friendly, welcoming language.

### Reasoning

The application should feel like a companion rather than a technical utility.

Example:

"Good morning, sunshine!"

---

## PD-003

### Decision

Festival information belongs on the dashboard.

### Reasoning

Festivals significantly influence player priorities and gold-making opportunities.

The dashboard should immediately communicate whether a festival is active.

---

## PD-004

### Decision

The dashboard prioritizes answering questions instead of displaying raw data.

### Reasoning

Recommendations should always appear before supporting information.

## PD-005

### Decision

TEO adopts a mascot to reinforce its identity.

### Reasoning

The mascot represents guidance, exploration and calm decision-making.

It should enhance the application's personality without distracting from its purpose.

### Impact

The mascot may appear in the dashboard, About page, documentation and branding, but should never interfere with usability.

## PD-006

The TEO interface should be visually calm and comfortable during long sessions.

### Reasoning

Players may keep TEO open for hours while playing Guild Wars 2.

The interface should reduce visual fatigue and avoid high-contrast or distracting elements.

### Impact

Favor muted colors, generous spacing, clear typography and subtle accents over flashy effects.

Dashboard panels follow a Question → Answer pattern. Labels ask the question; the value directly beneath answers it. This creates a consistent reading pattern across the entire application.

Knowledge stores facts. Reasoning interprets facts. Scout communicates decisions.

Knowledge describes the game. State describes today. Reasoning combines both. Scout communicates the result.

Goal-Driven Recommendations

Scout recommendations are always made in the context of the player's current goal.

Scout does not determine what the player should enjoy.

Instead, Scout answers the question:

"Given your goal today, what is the best next activity?"

Scout prioritizes opportunities but does not hide alternatives.