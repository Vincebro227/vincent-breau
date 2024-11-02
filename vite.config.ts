import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: '/vincent-breau/',
  plugins: [react()],
  server: {
    open: true
  }
});