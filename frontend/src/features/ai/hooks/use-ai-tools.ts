import { useMutation } from "@tanstack/react-query";
import {
  getGroupedTasks,
  getTaskPlan,
  improveExistingTask,
  improveTask,
} from "../api";

export function useAiTools() {
  const improveTaskMutation = useMutation({
    mutationFn: improveTask,
    onError: (error) => {
      console.error("Improve task error:", error);
    },
  });

  const improveExistingTaskMutation = useMutation({
    mutationFn: (taskId: number) => improveExistingTask(taskId),
    onError: (error) => {
      console.error("Improve existing task error:", error);
    },
  });

  const taskPlanMutation = useMutation({
    mutationFn: getTaskPlan,
    onError: (error) => {
      console.error("Get task plan error:", error);
    },
  });

  const groupedTasksMutation = useMutation({
    mutationFn: getGroupedTasks,
    onError: (error) => {
      console.error("Get grouped tasks error:", error);
    },
  });

  return {
    improveTaskMutation,
    improveExistingTaskMutation,
    taskPlanMutation,
    groupedTasksMutation,
  };
}