import { useEffect, useRef } from 'react'
import './App.css'

function App() {
  const wrapperRef = useRef()
  const gameRef = useRef()

//     if (screen.orientation && screen.orientation.lock) {
//   screen.orientation.lock("landscape").catch(err => {
//     console.warn('屏幕方向锁定失败', err)
//   })
// }


  const resize = () => {
  const w = window.innerWidth
  const h = window.innerHeight
  const aspect = 16 / 9
  const isPortrait = h > w

  const wrapper = wrapperRef.current
  const game = gameRef.current

  let gameW, gameH

  if (isPortrait) {
    // 🟢 真正以旋转后的横屏宽度（竖屏的高度）来适配
    gameW = h
    gameH = h / aspect
    wrapper.style.width = `${h}px`
    wrapper.style.height = `${w}px`
    wrapper.style.transform = `translate(-50%, -50%) rotate(90deg)`
  } else {
    // 🟢 横屏以屏幕高度为短边适配
    if (w / h > aspect) {
      gameH = h
      gameW = h * aspect
    } else {
      gameW = w
      gameH = w / aspect
    }
    wrapper.style.width = `${w}px`
    wrapper.style.height = `${h}px`
    wrapper.style.transform = `translate(-50%, -50%) rotate(0deg)`
  }

  game.style.width = `${gameW}px`
  game.style.height = `${gameH}px`
}


  useEffect(() => {
    resize()
    window.addEventListener('resize', resize)
    return () => window.removeEventListener('resize', resize)
  }, [])

  return (
    <div className="viewport">
      <div className="wrapper" ref={wrapperRef}>
        <div className="game" ref={gameRef}>
          <h1>强制横屏显示</h1>
          <p>16:9 比例，短边适配，旋转后仍保持一致</p>
        </div>
      </div>
    </div>
  )
}

export default App
