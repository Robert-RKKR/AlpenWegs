// Import component css:
import "./Pagination.css";

// Props for Pagination component:
type Props = {
  page: number;
  pageCount: number;
  onChange: (page: number) => void;
};

// Pagination Component:
export function Pagination({
  page,
  pageCount,
  onChange,
}: Props) {
  if (pageCount <= 1) {
    return null;
  }

  // Calculate page numbers to display (max 5 pages):
  const MAX_PAGES = 5;
  const half = Math.floor(MAX_PAGES / 2);

  let start = Math.max(1, page - half);
  let end = start + MAX_PAGES - 1;

  // Adjust when reaching the end:
  if (end > pageCount) {
    end = pageCount;
    start = Math.max(1, end - MAX_PAGES + 1);
  }

  const pages: number[] = [];

  // Add middle pages:
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }

  return (
    <div className="pagination">
      {/* First Page Button */}
      <button
        className={
          "pagination-item card-box" +
          (page === 1 ? " pagination-disabled" : "")
        }
        disabled={page === 1}
        onClick={() => onChange(1)}
      >
        First
      </button>

      {/* Previous Page Button */}
      <button
        className={
          "pagination-item card-box" +
          (page === 1 ? " pagination-disabled" : "")
        }
        disabled={page === 1}
        onClick={() => onChange(page - 1)}
      >
        Previous
      </button>

      {/* All Middle Pages Buttons */}
      {pages.map((p) => (
        <button
          key={p}
          className={
            p === page
              ? "pagination-item pagination-active card-box"
              : "pagination-item card-box"
          }
          disabled={p === page}
          onClick={() => onChange(p)}
        >
          {p}
        </button>
      ))}

      {/* Next Page Button */}
      <button
        className={
          "pagination-item card-box" +
          (page === pageCount ? " pagination-disabled" : "")
        }
        disabled={page === pageCount}
        onClick={() => onChange(page + 1)}
      >
        Next
      </button>

      {/* Last Page Button */}
      <button
        className={
          "pagination-item card-box" +
          (page === pageCount ? " pagination-disabled" : "")
        }
        disabled={page === pageCount}
        onClick={() => onChange(pageCount)}
      >
        Last
      </button>
    </div>
  );
}
