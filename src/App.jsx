import { useEffect, useRef } from 'react'
import './App.css'

function App() {
  const wrapperRef = useRef()
  const gameRef = useRef()

  const resize = () => {
    const w = window.innerWidth
    const h = window.innerHeight
    const aspect = 16 / 9
    const isPortrait = h > w

    let gameW, gameH
    if (w / h < aspect) {
      // 宽比高度还“瘦”，用宽度算高
      gameW = w
      gameH = w / aspect
    } else {
      // 高比宽度还“瘦”，用高度算宽
      gameH = h
      gameW = h * aspect
    }

    const wrapper = wrapperRef.current
    const game = gameRef.current

    // 设置 wrapper 尺寸和旋转
    if (isPortrait) {
      wrapper.style.width = `${h}px`
      wrapper.style.height = `${w}px`
      wrapper.style.transform = `translate(-50%, -50%) rotate(90deg)`
    } else {
      wrapper.style.width = `${w}px`
      wrapper.style.height = `${h}px`
      wrapper.style.transform = `translate(-50%, -50%) rotate(0deg)`
    }

    // 设置 game 尺寸（始终横屏）
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
