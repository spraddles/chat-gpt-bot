import { defineStore } from 'pinia'

export const useBaseStore = defineStore('store', {
	state: () => {
		return {
			loading: false,
		}
	},

	persist: {
		storage: persistedState.localStorage
	},

	actions: {

		clearStore() {
			this.$reset()
		}
	},

	getters: {}
})
