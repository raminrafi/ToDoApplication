import { userService } from '../_services';

const state = {
    all: {}
};

const actions = {
    getAllTask({commit}){
        commit('getAllTaskRequest');
        userService.getAllTasks()
            .then(tasks => commit('getAllTaskSuccess',tasks), errors=>commit('getAllTaskFailure',errors));
    },
    deleteTask({ commit }, id) {
        commit('deleteTaskRequest', id);

        userService.delete(id)
            .then(
                task => commit('deleteTaskSuccess', id),
                errors => commit('deleteTaskFailure', { id, errors: errors.toString() })
            );
    },
    createTask({dispatch,commit},task){
        commit('taskRequest', task);

        userService.createTask(task)
            .then(
                task => {
                    commit('taskSuccess', task);
                    router.push('/HomePage');
                    setTimeout(() => {
                        // display success message after route change completes
                        dispatch('alert/success', 'Task Created successfully', { root: true });
                    })
                },
                error => {
                    commit('taskFailure', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    }
};

const mutations = {
    getAllTaskRequest(state){
        state.all = {loading:true}
    },
    getAllTaskSuccess(state,task){
        state.all = {items: tasks};
    },
    getAllTaskFailure(state, errors) {
        state.all = { errors };
    },
    taskRequest(state, task) {
        state.status = { registering: true };
    },
    taskSuccess(state, task) {
        state.status = {};
    },
    taskFailure(state, error) {
        state.status = {};
    },
    deleteTaskRequest(state, id) {
        // add 'deleting:true' property to user being deleted
        state.all.items = state.all.items.map(task =>
            task.id === id
                ? { ...task, deleting: true }
                : task
        )
    },
    deleteTaskSuccess(state, id) {
        // remove deleted user from state
        state.all.items = state.all.items.filter(task => task.id !== id)
    },
    deleteTaskFailure(state, { id, error }) {
        // remove 'deleting:true' property and add 'deleteError:[error]' property to user
        state.all.items = state.items.map(task => {
            if (task.id === id) {
                // make copy of user without 'deleting:true' property
                const { deleting, ...userCopy } = task;
                // return copy of user with 'deleteError:[error]' property
                return { ...userCopy, deleteError: error };
            }

            return task;
        })
    }
};

export const tasks = {
    namespaced: true,
    state,
    actions,
    mutations
};


