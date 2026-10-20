# AGENTS.md

Проект работает по правилам из `.agents/`.

Перед любой реальной работой прочитай:

1. `.agents/AGENTS.md` — правила репозитория: границы слоёв, работа с БД и
   миграциями, запреты против обхода проверок, ворота готовности.
2. `.agents/CLAUDE.md` — карта правил и скилов.

Дальше выбери скил под задачу из `.agents/skills/<имя>/SKILL.md` (День 1):
`investigate-codebase`, `characterization-tests`, `tests-unit`, `tests-integration`,
`database-migration`, `fastapi-feature`, `safe-refactoring`. Тематические правила
лежат в `.agents/agents/`.

Не начинай менять код, пока не прочитал эти правила.
