import { defineConfig } from 'vite'
import { createVuePlugin } from '@vitejs/plugin-vue2'

export default defineConfig({
  plugins: [
    createVuePlugin()
  ],
  server: {
    port: 3000
  }
}) 