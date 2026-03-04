# Yummy Pizza AI Agent

An autonomous pizza ordering chatbot built with LangChain, Streamlit, and LLM.

## Project Structure

```
pizza-chatbot/
├── app.py                  # Main Streamlit app
├── requirements.txt
├── agent/
│   ├── pizza_agent.py      # LangChain + Ollama agent
│   └── prompts.py          # System prompt
├── data/
│   └── menu.py             # Menu items & prices
├── utils/
│   ├── bill_calculator.py  # Bill + GST calculator
│   └── qr_generator.py     # UPI QR code generator
└── assets/
    └── pizza_ready.png     # Order confirmed image
```

## User Flow

1. Agent greets user
2. User browses menu (sidebar or chat)
3. User places order via chat
4. Bill with GST shown (a demo)
5. UPI QR code generated for payment (Random demo QR via python qr librabry)
6. Order confirmed with estimated pickup time (Random)
7. Pizza image displayed!(demo image)

## Tips

- Type `menu` to see the full menu
- Say `I want to pay` or `confirm order` to trigger bill
- Click "Start New Order" in sidebar to reset
