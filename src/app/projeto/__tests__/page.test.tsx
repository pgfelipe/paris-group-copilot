import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import ProjetoPage from '../page'

test('rota /projeto mostra o título "Projeto"', () => {
  render(<ProjetoPage />)
  expect(screen.getByRole('heading', { level: 1, name: 'Projeto' })).toBeDefined()
})
