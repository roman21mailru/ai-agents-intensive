// Workshop plugin: intentionally idle on session.start (no auto LLM call).
export const LoadRules = async () => {
  return {
    event: async () => {},
  };
};
