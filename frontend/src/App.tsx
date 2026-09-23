import { Route, Routes } from 'react-router'

import Layout from './components/Layout'
import Home from './pages/Home'
import Applications from './pages/Applications'
import Interviews from './pages/Interviews'
import Login from './pages/Login'


function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/applications" element={<Applications />} />
        <Route path="/interviews" element={<Interviews />} />
      </Route>
    </Routes>
  )
}

export default App