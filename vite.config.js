import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/testweb/', // 部署到github仓库就写仓库名，部署到自定义域名（无后缀）就写'/'
  plugins: [react()],
})

