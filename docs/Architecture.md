# TEO Architecture

Version: 1.0

---

# Purpose

The purpose of this document is to define the architecture of the Tyrian Economic Optimizer (TEO).

This document is intended to remain stable throughout the lifetime of the project and should only change when a major architectural decision is made.

---

# Design Principles

TEO follows several core principles.

## 1. Single Source of Truth

Every piece of information exists only once.

Examples:

- Fish information exists only in the database.
- Map information exists only in the database.
- Market prices exist only in the database.
- Calculations never duplicate stored data.

---

## 2. Data First

TEO separates data from logic.

The database stores facts.

The application interprets those facts.

Example:

Database:

Halibut

Fishing Hole:
Boreal

Preferred Bait:
Shrimplings

Logic:

Which bait should the player use?

---

## 3. Decision Engine

The Decision Engine is the heart of TEO.

Modules never make recommendations directly.

Modules provide data.

The Decision Engine evaluates that data and generates recommendations.

Example:

Fishing Module

↓

Fish statistics

↓

Decision Engine

↓

"Fish in Thunderhead Peaks."

---

## 4. Modular Design

Each feature belongs to its own module.

Examples:

Fishing

Trading Post

Crafting

Currencies

Routes

Achievements

Modules should never contain unrelated functionality.

---

## 5. Reusable Components

Logic should only be written once.

If multiple modules need the same functionality, it belongs in a shared component.

---

## 6. Explainable Decisions

Every recommendation made by TEO should be explainable.

If TEO recommends a map, route or activity, it should also explain why that recommendation was made.

---

# High-Level Architecture

                  User Interface
                         │
                         ▼
                 Decision Engine
                 /      |      \
                /       |       \
         Fishing   Economy   Trading
                \       |       /
                 \      |      /
                    Database

The database stores facts.

Modules retrieve information.

The Decision Engine evaluates the information.

The User Interface displays the results.

---

# Project Layers

Layer 1

User Interface

Responsibilities

• Display information

• Collect user input

• Never contain business logic

---

Layer 2

Decision Engine

Responsibilities

• Evaluate information

• Calculate profitability

• Score activities

• Rank recommendations

---

Layer 3

Modules

Responsibilities

• Retrieve information

• Perform feature-specific calculations

• Never make recommendations

---

Layer 4

Database

Responsibilities

• Store all persistent information

• Maintain relationships

• Act as the single source of truth

---

# Core Values

## Accuracy

Recommendations should be based on verified game mechanics and reliable data.

## Transparency

Users should always understand why TEO made a recommendation.

## Practicality

Recommendations should reflect real gameplay, not theoretical maximums.

## Simplicity

Complex calculations should produce simple recommendations.

## Maintainability

Every feature should be designed so it can continue to work after future Guild Wars 2 expansions.

# Database Philosophy

SQLite is the primary data store.

JSON is used only for:

• Import

• Export

• Sample data

The database always has priority over JSON.

---

# User Interface Philosophy

The interface should answer one question quickly:

"What should I do next?"

Information should be:

• Easy to understand

• Data-driven

• Explainable

• Consistent

---

# Future Expansion

TEO is designed to support additional modules without changing its architecture.

Potential future modules include:

Fishing

Crafting

Trading Post

Currencies

Gathering

Meta Events

Home Instance

Wizard's Vault

Character Planner

Legendary Crafting

Market Analytics

Festival Optimizer

---

# Coding Standards

The project values:

Readability over cleverness.

Maintainability over shortcuts.

Documentation over assumptions.

Simple solutions over complex ones.

---

# Project Goal

TEO should become the most comprehensive decision support application for Guild Wars 2 while remaining easy to understand, easy to extend and easy to maintain.

## Knowledge Engine

The Knowledge Engine is responsible for answering questions about Guild Wars 2.

It exposes simple query functions such as:

- get_current_festival()
- get_next_festival()

The user interface never accesses resource files directly.

TEO provides guidance and links players to authoritative community resources rather than duplicating large amounts of reference information.