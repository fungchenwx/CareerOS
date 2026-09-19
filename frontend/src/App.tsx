import { Route, Routes } from 'react-router'

import Home from './pages/Home'
import Applications from './pages/Applications'
import Interviews from './pages/Interviews'

import { Route, Routes } from 'react-router'

import Home from './pages/Home'
import Applications from './pages/Applications'
import Interviews from './pages/Interviews'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/applications" element={<Applications />} />
      <Route path="/interviews" element={<Interviews />} />
    </Routes>
  )
}

export default App