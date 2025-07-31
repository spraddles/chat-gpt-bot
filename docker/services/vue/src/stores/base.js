import { defineStore } from 'pinia'

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const useBaseStore = defineStore('store', {
	state: () => {
		return {
			loading: false,
		}
	},

	actions: {

		clearStore() {
			this.$reset()
		},

        async sendChat(prompt, maxLength = 50, temperature = 0.25) {
            const res = await fetch(`${BASE_URL}/api/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    prompt,
                    max_length: maxLength,
                    temperature,
                }),
            })

            if (!res.ok) {
                const errorText = await res.text()
                throw new Error(`Chat API error ${res.status}: ${errorText}`)
            }

            const { response } = await res.json()
            return response
        }
	},

	getters: {}
})
