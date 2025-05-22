import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/testweb/', // 部署到github仓库就写仓库名，部署到自定义域名（无后缀）就写'/'
  plugins: [react()],
})


// import { VitePWA } from 'vite-plugin-pwa'
// VitePWA({
//   filename: 'sw-beyond.js',  // Service Worker 文件名（默认是 sw.js），这里为避免命名冲突做了改名
//   scope: '/',                // 作用范围，配合 base 设置，表示全站生效
//   registerType: 'autoUpdate',// 注册模式，自动更新 service worker
//   manifest: {
//     name: '世界之外 抽卡模拟器',       // 应用完整名称（安装后显示）
//     short_name: '世外抽卡',            // 安装后在主屏幕上的显示名
//     start_url: '/',                   // PWA 启动时打开的页面
//     display: 'standalone',           // 启动样式，`standalone` 表示像原生 app 一样（无地址栏等）
//     background_color: '#ffffff',     // 启动画面背景色
//     icons: [                          // 应用图标，用于安装在桌面
//       {
//         src: 'https://cdn.chenczn3528.dpdns.org/beyondworld/images/icon.jpg',
//         sizes: '512x512',
//         type: 'image/png'
//       }
//     ]
//   },
//   cleanupOutdatedCaches: true, // 自动清除旧版本缓存
// })
