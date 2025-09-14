## PR #10: DOC-3: Add BFS and DFS functionality modes for graph traversal alongs…
*Merged:* 2025-09-14 • *Author:* AkramUmad572 • *Base:* main ← *Head:* DOC-3-add-jira
### Summary
## DOC-3: Add BFS and DFS Graph Traversal Modes

**1. Summary**

This pull request enhances graph traversal capabilities by adding Breadth-First Search (BFS) and Depth-First Search (DFS) functionality alongside the existing Dijkstra's algorithm.  This provides more versatile graph traversal options.

**2. Technical Changes**

Added BFS and DFS algorithms as new modes for graph traversal.  The implementation allows users to select the desired traversal method.

**3. Risks/Edge Cases**

* **Performance:**  The performance of BFS and DFS may vary depending on graph structure and size.  Testing should be conducted to ensure acceptable performance across various scenarios.
* **Error Handling:** Robust error handling should be implemented to manage cases such as empty graphs or invalid input.

**4. Docs/Follow-ups**

* Update documentation to reflect the addition of BFS and DFS modes, including usage examples and performance considerations.
* Add unit tests to cover the new functionality and edge cases.
### Technical Changes
- DOC-3: Add BFS and DFS functionality modes for graph traversal alongside dijstras
### Risks / Edge Cases
- (fill in if applicable; e.g., migration, perf, feature flag rollout)
### Rollback Plan
- Use GitHub “Revert” on PR #10 (auto-creates a revert PR).
- Undo any external side effects (migrations/config/docs).
### Docs / Follow-ups
- (list docs to update or follow-up tasks/tickets/owners)
### Links
- PR: https://github.com/AkramUmad572/htn25-test/pull/10
- Diff: https://github.com/AkramUmad572/htn25-test/compare/9e32f8c024fde2908751753da6e77ea34837e3e4...4ae68c9c42baadb457c88a462bd761c36b36d470
---
## PR #11: Revert "DOC-3: Add BFS and DFS functionality modes for graph traversal alongs…"
*Merged:* 2025-09-14 • *Author:* AkramUmad572 • *Base:* main ← *Head:* revert-10-DOC-3-add-jira
### Summary
## Revert of Graph Traversal Functionality

**1. Summary**

This pull request reverts commit AkramUmad572/htn25-test#10, which added Breadth-First Search (BFS) and Depth-First Search (DFS) functionality for graph traversal.  The reason for the revert is not explicitly stated in the provided information.

**2. Technical Changes**

The pull request simply undoes the addition of BFS and DFS graph traversal modes.  No new code is introduced; only the previously added code is removed.

**3. Risks/Edge Cases**

The risks are associated with the original changes that are now reverted.  Without knowing the specifics of AkramUmad572/htn25-test#10, potential risks are unknown.  However, reverting the changes might reintroduce any bugs or issues that the original commit was intended to fix.

**4. Docs/Follow-ups**

No documentation updates are needed as the changes are a complete revert.  Further investigation into why the original changes were reverted is recommended.  If the functionality is desired, a new PR with improved implementation should be created.
### Technical Changes
- Revert "DOC-3: Add BFS and DFS functionality modes for graph traversal alongs…"
### Risks / Edge Cases
- (fill in if applicable; e.g., migration, perf, feature flag rollout)
### Rollback Plan
- Use GitHub “Revert” on PR #11 (auto-creates a revert PR).
- Undo any external side effects (migrations/config/docs).
### Docs / Follow-ups
- (list docs to update or follow-up tasks/tickets/owners)
### Links
- PR: https://github.com/AkramUmad572/htn25-test/pull/11
- Diff: https://github.com/AkramUmad572/htn25-test/compare/358c5f983bd5811d2d00f48ed28f3b647c9ea16e...0512257b2238caae6c2ad9febcd89fb3dc13597a
---
## PR #10: DOC-3: Add BFS and DFS functionality modes for graph traversal alongs…
*Merged:* 2025-09-14 • *Author:* AkramUmad572 • *Base:* main ← *Head:* DOC-3-add-jira
### Summary
## DOC-3: Add BFS and DFS Graph Traversal Modes

**1. Summary**

This pull request enhances graph traversal capabilities by adding Breadth-First Search (BFS) and Depth-First Search (DFS) functionalities alongside the existing Dijkstra's algorithm.  This provides more versatile graph traversal options.

**2. Technical Changes**

Added new functions implementing BFS and DFS algorithms for graph traversal.  These functions are integrated to offer users a choice of traversal method.

**3. Risks/Edge Cases**

No specific risks or edge cases identified in the PR description.  Thorough testing is recommended to cover various graph structures and sizes.

**4. Docs/Follow-ups**

Documentation should be updated to reflect the addition of BFS and DFS functionalities, including usage examples and explanations of their differences compared to Dijkstra's algorithm.  Unit tests should be added to ensure the correctness and robustness of the new implementations.
### Technical Changes
- DOC-3: Add BFS and DFS functionality modes for graph traversal alongside dijstras
### Risks / Edge Cases
- (fill in if applicable; e.g., migration, perf, feature flag rollout)
### Rollback Plan
- Use GitHub “Revert” on PR #10 (auto-creates a revert PR).
- Undo any external side effects (migrations/config/docs).
### Docs / Follow-ups
- (list docs to update or follow-up tasks/tickets/owners)
### Links
- PR: https://github.com/AkramUmad572/htn25-test/pull/10
- Diff: https://github.com/AkramUmad572/htn25-test/compare/9e32f8c024fde2908751753da6e77ea34837e3e4...4ae68c9c42baadb457c88a462bd761c36b36d470
---
## PR #9: DOC-3: adding logic change to path finding algorithm in path_finder.p…
*Merged:* 2025-09-14 • *Author:* AkramUmad572 • *Base:* main ← *Head:* DOC-3-add-jira
### Summary
1. **Summary**

This pull request enhances the pathfinding algorithm within the `path_finder.py` module.  The changes improve the algorithm's logic and include comprehensive documentation, crucial given the module's use across multiple other modules.

2. **Technical Changes**

The pull request modifies the pathfinding algorithm in `path_finder.py`.  Specific details about the algorithm changes are not provided in the description.  The implementation emphasizes thorough documentation.

3. **Risks/Edge Cases**

No risks or edge cases are explicitly identified in the pull request description.  Further investigation may be needed to assess potential issues.

4. **Docs/Follow-ups**

The pull request focuses on improving documentation for the `path_finder.py` module.  No further documentation or follow-up tasks are specified.
### Technical Changes
- DOC-3: adding logic change to path finding algorithm in path_finder.py which is a module which will be used in multiple other modules so the implementation must be well documented
### Risks / Edge Cases
- (fill in if applicable; e.g., migration, perf, feature flag rollout)
### Rollback Plan
- Use GitHub “Revert” on PR #9 (auto-creates a revert PR).
- Undo any external side effects (migrations/config/docs).
### Docs / Follow-ups
- (list docs to update or follow-up tasks/tickets/owners)
### Links
- PR: https://github.com/AkramUmad572/htn25-test/pull/9
- Diff: https://github.com/AkramUmad572/htn25-test/compare/374d19af0d6a721e9733a9b1ec2ce62c2ab6ebe1...9e5978fca51b1266ad151cca6aa47589d824b915
---
## REVERT of PR #8: DOC-3: add comment for hello world in python file
*Reverted:* 2025-09-14 • *Original Merge:* 2025-09-14T10:24:13Z • *Author:* AkramUmad572
### Summary
This entry documents a revert of the original change introduced by PR #8. No prior changelog entries were removed; the log remains append-only.
### What Changed
- Code reverted to the first parent of merge commit `fcb51ae81f6dcf78a46ec2a115a694b4f73ec4a0` via new commit `9d352cda650916ac561e1ae90ebf883b0f66aa6d`.
- Documentation: earlier entries remain intact; this entry records the revert.
### Links
- Original PR: https://github.com/AkramUmad572/htn25-test/pull/8
- Merge commit: `fcb51ae81f6dcf78a46ec2a115a694b4f73ec4a0`
- Revert commit: `9d352cda650916ac561e1ae90ebf883b0f66aa6d`
---
## PR #7: DOC-3: add hello world in jira.py new file
*Merged:* 2025-09-14 • *Author:* AkramUmad572 • *Base:* main ← *Head:* DOC-3-add-jira
### Summary
## DOC-3: Add "Hello, World" to jira.py

**1. Summary**

This pull request adds a new file, `jira.py`, containing a simple "Hello, World" program.  No further context or functionality is provided.

**2. Technical Changes**

A new file, `jira.py`, was created and contains a basic "Hello, World" program.  No other code changes were made.

**3. Risks/Edge Cases**

None identified, given the minimal nature of the change.  The purpose of this commit is unclear without further context.

**4. Docs/Follow-ups**

The purpose and intended use of `jira.py` require clarification.  Further documentation is needed to explain its function and integration within the larger project.
### Technical Changes
- DOC-3: add hello world in jira.py new file
### Risks / Edge Cases
- (fill in if applicable; e.g., migration, perf, feature flag rollout)
### Rollback Plan
- Use GitHub “Revert” on PR #7 (auto-creates a revert PR).
- Undo any external side effects (migrations/config/docs).
### Docs / Follow-ups
- (list docs to update or follow-up tasks/tickets/owners)
### Links
- PR: https://github.com/AkramUmad572/htn25-test/pull/7
- Diff: https://github.com/AkramUmad572/htn25-test/compare/fd61fdad30deba92677faabe230b5847d7f579d4...beb17e200c8114be021d8956304111911b41e1b2
---

