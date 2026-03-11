# GitHub Secrets: Treasure Hunt 🔐

## Overview

Dr. Obeid has hidden a secret message in a private repository. You can't access it directly — but you *can* if you have the right key.

In this activity, you'll:
1. Store a secret key in your GitHub repository
2. Use that key in a GitHub Actions workflow
3. Authenticate to access the hidden treasure

This is exactly how real applications handle credentials for databases, APIs, and deployments.

---

## Instructions

### Step 1: Set Up Your Repository

Fork this repository to your local github account.

### Step 2: Get the Key

Dr. Obeid will briefly display a **Personal Access Token (PAT)** on screen. Copy it immediately — this is your treasure key.

### Step 3: Add the Secret

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `TREASURE_KEY`
5. Value: *(paste the PAT)*
6. Click **Add secret**

### Step 4: Push and Run

In GitHub, go to Actions and manually trigger the "Fetch the Treasure" action.

Watch the magic happen and see if you can see the secret message.

---

## What Success Looks Like

```
🔐 Attempting to access the private treasure...

✅ SUCCESS! You found the treasure!

========== SECRET MESSAGE ==========
🎉 CONGRATULATIONS! 🎉

You successfully authenticated using a secret!
...
====================================

🎉 Your secret is working correctly!
```

---

## What Failure Looks Like

**If you forgot to add the secret:**
```
❌ UNAUTHORIZED (401)
   Your TREASURE_KEY secret is missing or invalid.
   Did you add it in Settings → Secrets → Actions?
```

**If the username is wrong:**
```
❌ NOT FOUND (404)
   The treasure repo or file doesn't exist.
   Check with your instructor.
```

---

## How It Works

```yaml
- name: Fetch the treasure
  env:
    TREASURE_KEY: ${{ secrets.TREASURE_KEY }}
  run: |
    curl -H "Authorization: Bearer $TREASURE_KEY" \
      "https://raw.githubusercontent.com/INSTRUCTOR/repo/main/treasure.txt"
```

1. `${{ secrets.TREASURE_KEY }}` pulls the secret from GitHub's encrypted storage
2. The secret is injected as an environment variable
3. `curl` uses it in the `Authorization` header to authenticate
4. GitHub's API grants access to the private file

Without the key? Access denied.

---

## Submission

Screenshot your successful workflow run showing the secret message. Submit via Canvas->Assignments->Fetch Treasure Assignment.

---

## Next Challenge
Write a short Python program that uses the `TREASURE_KEY` secret to access the secret message (instead
of having the `fetch-treasure.yml` workflow do all the work.) 

You should be able to run this python command locally to see the message.

You should also create a workflow file so that the code can access the secret message in GitHub and successfully read the message.

Reminder, the secret message is located at:

`https://raw.githubusercontent.com/iyad-obeid/secret-message/main/treasure.txt`

---

## Key Takeaways

| Concept | What You Learned |
|---------|------------------|
| **Secrets storage** | GitHub encrypts secrets, never displays them after saving |
| **Secrets injection** | Use `${{ secrets.NAME }}` to access in workflows |
| **Authentication** | Secrets let you access protected resources |
| **Principle of least privilege** | The PAT only has read access to one repo |

---

## Real-World Applications

This same pattern is used for:
- 🗄️ Database credentials in production deployments
- 🔑 API keys for third-party services (Stripe, AWS, etc.)
- 🚀 Deployment tokens for Heroku, Azure, AWS
- 📦 Package registry tokens for npm, PyPI

Now you know how it works!
